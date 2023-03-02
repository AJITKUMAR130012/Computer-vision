# -*- coding: utf-8 -*-
"""Computer_vision_Assignment1_10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Otg5lSE7RjaDI4_3Wjm8cbMYnDUe5H5x
"""

!git clone https://github.com/AJITKUMAR130012/Computer-vision.git

cd Computer-vision

cd Assignment1

!pip install easyocr

import numpy as np
import pandas as pd
import cv2
import easyocr
import matplotlib.pyplot as plt

img1=cv2.imread("./Dataset/10/Screenshot 2023-01-08 at 5.14.24 PM.png")
img2=cv2.imread("./Dataset/10/Screenshot 2023-01-08 at 5.14.47 PM.png")

plt.subplot(1,2,1)
plt.imshow(img1)
plt.subplot(1,2,2)
plt.imshow(img2)
plt.show()

reader = easyocr.Reader(['en'])
result1 = reader.readtext(img1)
result2= reader.readtext(img2)

print(result1)

print(result2)

print((result1[0][1][-3:]))

print((result2[0][1][-3:]))
