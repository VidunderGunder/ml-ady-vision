# MLAdy Vision

All things related to vision

## Quick start

_Note: Only tested on Windows 10, using Anaconda PowerShell_

Install [Anaconda](https://www.anaconda.com/products/individual#Downloads)

Install [CUDA 11.0 (Update 1)](https://developer.nvidia.com/cuda-11.0-update1-download-archive)

Install [cuDNN 8.0.4 for CUDA 11.0](https://developer.nvidia.com/rdp/cudnn-archive)

Open an Anaconda PowerShell Prompt in project root

Create virtual environmet

```ps
conda create -n vision python=3.8
```

Activate virtual environmet

```ps
conda activate vision
```

Install PyTorch with CUDA/cuDNN-support

```ps
conda install pytorch torchvision torchaudio cudatoolkit=11.0 -c pytorch
```

Install required packages for TACO

```ps
pip install -r yolov5/requirements.txt
```

Install required packages for YOLOv5

```ps
pip install -r TACO/requirements.txt
pip install git+https://github.com/philferriere/cocoapi.git#subdirectory=PythonAPI
```

Download TACO-dataset

```ps
cd TACO
python download.py
```

Go back to project root

```ps
cd ..
```

Install packages required for `taco2yolo.py`

```ps
pip install split-folders
```
 
Convert TACO to YOLO

```ps
python taco2yolo.py
```

Train YOLOv5 on TACO-dataset

```ps
cd yolov5
python train.py --data taco.yaml --img-size 128 --cfg yolov5s.yaml --weights yolov5s.pt --device 0 --batch-size 4
```

_Note: Parameters meant for testing only_

## Hardware

Tested on:

- OS: Windows 10 Pro
- GPU: RTX 2070 8GB
- CPU: Intel Xeon W-2125
- RAM: 16GB