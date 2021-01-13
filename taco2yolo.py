# %%
import os
import shutil
import numpy as np
import tqdm
from pycocotools.coco import COCO
import splitfolders

# import argparse

# %%

# parser = argparse.ArgumentParser(description="")
# parser.add_argument(
#     "--in_path",
#     required=False,
#     default="./drive/MyDrive/ml-ady-data/taco/",
#     help="Path to taco data (input)",
# )
# parser.add_argument(
#     "--out_path",
#     required=False,
#     default="./drive/MyDrive/ml-ady-data/yolo/",
#     help="Path to yolo data (output)",
# )
# args = parser.parse_args()

in_path = "./drive/MyDrive/ml-ady-data/taco/"  # Path to taco data (input)
out_path = "./drive/MyDrive/ml-ady-data/yolo/"  # Path to yolo data (output)

data = COCO(annotation_file=in_path + "annotations.json")

# %%
# Get classes,

img_ids = data.getImgIds()

catIds = data.getCatIds()
categories = data.loadCats(catIds)
categories.sort(key=lambda x: x["id"])
classes = {}
coco_labels = {}
coco_labels_inverse = {}

for category in categories:
    coco_labels[len(classes)] = category["id"]
    coco_labels_inverse[category["id"]] = len(classes)
    classes[category["name"]] = len(classes)

class_num = {}

# %%
# import pprint

# pp = pprint.PrettyPrinter(indent=4)

# print("\n\ncatIds:\n")
# pp.pprint(catIds)
# print("\n\ncategories:\n")
# pp.pprint(categories)
# print("\n\ncategories:\n")
# pp.pprint(categories)
# print("\n\nclasses:\n")
# pp.pprint(classes)
# print("\n\ncoco_labels:\n")
# pp.pprint(coco_labels)
# print("\n\ncoco_labels_inverse:\n")
# pp.pprint(coco_labels_inverse)
# print("\n\nclass_num:\n")
# pp.pprint(class_num)

# %%
# Create temporary folders

yolo_data_all_path = out_path + "all/"
save_base_path = yolo_data_all_path + "labels/"
save_image_path = yolo_data_all_path + "images/"

folders = [save_base_path, save_image_path]

for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)

# %%
# Turn TACO images and labels to YOLO

label_transfer = {5: 0, 12: 1}

for index, img_id in tqdm.tqdm(
    enumerate(img_ids),
    desc="Convert annotations from JSON to TXT",
):
    img_info = data.loadImgs(img_id)[0]
    save_name = img_info["file_name"].replace("/", "_")
    file_name = save_name.split(".")[0]
    height = img_info["height"]
    width = img_info["width"]
    save_path = save_base_path + file_name + ".txt"
    # exists = False
    with open(save_path, mode="w") as fp:
        annotation_id = data.getAnnIds(img_id)
        boxes = np.zeros((0, 5))
        if len(annotation_id) == 0:
            fp.write("")
            continue
        annotations = data.loadAnns(annotation_id)
        lines = ""
        for annotation in annotations:
            label = coco_labels_inverse[annotation["category_id"]]
            # if label in label_transfer.keys():
            # exists = True
            box = annotation["bbox"]
            if box[2] < 1 or box[3] < 1:
                continue
            # top_x,top_y,width,height==>cen_x,cen_y,width,height
            box[0] = round((box[0] + box[2] / 2) / width, 6)
            box[1] = round((box[1] + box[3] / 2) / height, 6)
            box[2] = round(box[2] / width, 6)
            box[3] = round(box[3] / height, 6)
            # label = label_transfer[label]
            label = 0
            if label not in class_num.keys():
                class_num[label] = 0
            class_num[label] += 1
            lines = lines + str(label)
            for i in box:
                lines += " " + str(i)
            lines += "\n"
        fp.writelines(lines)
    # if exists:
    shutil.copy(
        in_path + img_info["file_name"],
        os.path.join(save_image_path, save_name),
    )
    # else:
    # os.remove(save_path)

# %%
splitfolders.ratio(
    yolo_data_all_path,
    output=out_path + "split",
    seed=42,
    # Train, validation, test
    ratio=(0.8, 0.1, 0.1),
)
