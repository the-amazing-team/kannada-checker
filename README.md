# Kannada Checker

## Problem Statement and Motivation

Our project aims to address the challenge of determining and fulfil the extent of local or regional language usage on name boards of businesses and startups. By leveraging image processing techniques coupled with text extraction tools like EasyOCR and language detection libraries, the project seeks to calculate the percentage of local language content on these boards. This analysis serves to understand and encourage the use of regional languages in business representations, promoting inclusivity and cultural significance within communities .

## Installation

Before running the project, please ensure that you run the following commands to install the required dependencies:

```bash
pip install -r requirements.txt
```

You will find that few sample images have been provided in the `dataset` folder. You can add your own images to this folder and run the project to see the results.

To compile and test the project on these samples, run the following command:

```bash
python main.py
```

You will find the results in the `annotated` folder.

## Approach / Workflow

### Dataset

The dataset consists of 52 images collected randomly from Google Images. It has been ensured that the images are of high quality and are not blurred. Various images of all amount of text in both and Kannada and English have been included.

You can find the dataset in the `dataset` folder.

### Dependencies

#### OpenCV

OpenCV is a library of programming functions mainly aimed at real-time computer vision. Originally developed by Intel, it was later supported by Willow Garage then Itseez. The library is cross-platform and free for use under the open-source Apache 2 License. OpenCV supports the deep learning frameworks TensorFlow, Torch/PyTorch and Caffe.

#### EasyOCR

EasyOCR is a python package that allows one to extract text from images and PDFs. It is a re-implementation of the popular C++ package, Tesseract, and is a part of the EasyOCR family of packages. EasyOCR is a single-function package that is easy to use and can be used to extract text from images and PDFs.

#### Translate

Translate is a python package that allows one to translate text from one language to another. It is a part of the EasyOCR family of packages. Translate is a single-function package that is easy to use and can be used to translate text from one language to another.

#### TQDM

TQDM is a progress bar library with good support for nested loops and Jupyter/IPython notebooks.

#### langdetect

langdetect is a python package that allows one to detect the language of a text. It is a part of the EasyOCR family of packages. langdetect is a single-function package that is easy to use and can be used to detect the language of a text.

### Approach

## Results, Dicussion & Future Work

### Results

### Future Plans
