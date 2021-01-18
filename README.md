# MLAdy Vision <!-- omit in toc -->

All things related to vision 👀

![vision](docs/vision.jpg)

## Table of Contents <!-- omit in toc -->

- [Detection 🔍](#detection-)
  - [Quick Start 🚀](#quick-start-)
- [Depth 🤽‍♂️](#depth-️)
  - [Quick Start 🚀](#quick-start--1)

## Detection 🔍

[YOLOv5](https://github.com/ultralytics/yolov5) with custom training to detect trash

See `train_trash_detection.ipynb` for training

Datasets used for training:

- [TACO](http://tacodataset.org/)

### Quick Start 🚀

[Download the custom weights](https://drive.google.com/file/d/12bzxSK9DIJaJYcg5py_qm-pkxRrJr94k/view?usp=sharing)

Place them in the project's root

Go into the `yolov5` folder

```sh
cd yolov5
```

Install requirements

```sh
pip install -r requirements.txt
```

Run inference

```shell
python detect.py --source "../input/trash.jpg" --weights "../detection_weights.pt" --img-size 640 --conf 0.675 --exist-ok --project ../ --name output
```

## Depth 🤽‍♂️

[AdaBins](https://github.com/shariqfarooq123/AdaBins) with pretrained models to estimate depth map

Datasets used for training:

- [KITTI](http://www.cvlibs.net/datasets/kitti/eval_depth_all.php) *outdoors*
- [NYU](https://cs.nyu.edu/~silberman/datasets/nyu_depth_v2.html) *indoors*


### Quick Start 🚀

_The guide requires an NVIDIA GPU with CUDA-support._  
_CPU-only inference works, but training wise you're on your own._

Install [CUDA](https://developer.nvidia.com/cuda-toolkit-archive) (tested on 10.2)

Install [cuDNN](https://developer.nvidia.com/rdp/cudnn-download) (tested on 8.0.5 for CUDA 10.2)

Install [Anaconda](https://www.anaconda.com/products/individual).

Create virtual environment (tested on python 3.6.6)

```sh
conda create -n vision python=3.6.6 anaconda
```

Install PyTorch (tested on 1.7.0 and 1.7.1)

```sh
conda install pytorch torchvision torchaudio cudatoolkit=10.2 -c pytorch
```

See [get started](https://pytorch.org/get-started/locally/) if not following previous recommendations, as you may want another version of PyTorch.

Install Taqaddum

```sh
conda install -c conda-forge tqdm
```

Run the setup

```sh
setup_depth.sh
```

[Download pretrained weights](https://drive.google.com/drive/folders/1nYyaQXOBjNdUJDsmJpcRpu6oE55aQoLA?usp=sharing)

Place pretrained weights in `pretrained/`

Test depth inference

```sh
python depth.py
```
