git clone https://github.com/shariqfarooq123/AdaBins.git
mkdir pretrained
fileid=1lvyZZbC9NLcS8a__YPcUP7rDiIpbRpoF
filename=AdaBins_nyu.pt
echo " Downloading models..."
ids=1lvyZZbC9NLcS8a__YPcUP7rDiIpbRpoF,1nYyaQXOBjNdUJDsmJpcRpu6oE55aQoLA 
curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=${fileid}" > /dev/null
curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=${fileid}" -o "./pretrained/"${filename}
fileid=1nYyaQXOBjNdUJDsmJpcRpu6oE55aQoLA
filename=AdaBins_kitti.pt
curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=${fileid}" > /dev/null
curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=${fileid}" -o "./pretrained/"${filename}