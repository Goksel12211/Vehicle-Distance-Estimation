# Vehicle-Distance-Estimation 
## Purpose
This project's purpose is determining the distance between two vehicles .

## Technologies
- Python3
- Yolov3
- OpenCv
- Tkinter
- Pillow
- Numpy

## General Info
In this project, it was written in Python coding language and the yolov3 model available here was used.

Object detection was made using yolov3, and the distances between these objects were calculated with the Euclidean Distance Calculation Algorithm. By looking at the objects for which the distances between them were calculated, it was determined that the values below 2 meters (200 cm) violated the distance and these vehicles were shown with a red box.

The video was taken and displayed on the screen using the tkinter library and cv2 as a gui.

## ScreenShoot
![alt text](https://github.com/Goksel12211/Vehicle-Distance-Estimation/blob/main/input/demo.png?raw=true)

## Setup
To run this app, you will need to follow these 3 steps:

#### 1. Requirements
- a Laptop

- Text Editor or IDE (eg. vscode, PyCharm)

- Git installed on your Laptop.

#### 2. Install Python and Pipenv
- <a href="https://www.python.org/downloads/release/python-3101/">Python3<i height="28"></a>

- <a href="https://pipenv-es.readthedocs.io/es/stable/">Pipenv<i height="28"></a>
#### 3. Local Setup and Running on Windows, Linux and Mac OS

  ```
  # Clone this repository into the directory of your choice
  $ git clone https://github.com/Goksel12211/Vehicle-Distance-Estimation.git
  
  # Move into project folder
  $ cd Vehicle-Distance-Estimation
  
  # Install from Pipfile
  $ pipenv install -r requirements.txt 
  
  # Activate the Pipenv shell
  $ pipenv shell
  ```
#### Contributors
  <table>
  <tr>
    <td align="center"><a href="https://github.com/Goksel12211"><img src="https://avatars.githubusercontent.com/Goksel12211?v=4" width="100px;" alt=""/><br /><sub><b>Göksel Kınalı</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/ysfArslan1"><img src="https://avatars.githubusercontent.com/ysfArslan1?v=4s=100" width="100px;" alt=""/><br /><sub><b>Yusuf Arslan</b></sub></a><br /></td>
<td align="center"><a href="https://github.com/oguzhankoc55"><img src="https://avatars.githubusercontent.com/oguzhankoc55?v=4s=100" width="100px;" alt=""/><br /><sub><b>Oğuzhan Koç </b></sub></a><br /></td>
<td align="center"><a href="https://github.com/caglaozbb"><img src="https://avatars.githubusercontent.com/caglaozbb?v=4s=100" width="100px;" alt=""/><br /><sub><b>Çağla Özbaba </b></sub></a><br /></td>

  </tr>
  
</table>

