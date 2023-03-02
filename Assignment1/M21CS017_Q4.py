# -*- coding: utf-8 -*-
"""Computer_vision_Assignment1_4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nqjwA6tMEyIwWKRhvCll0qGtwEwLlfdO
"""

!git clone https://github.com/AJITKUMAR130012/Computer-vision.git

cd Computer-vision

!ls

cd Assignment1

import numpy as np
import pandas as pd
from skimage.transform import (hough_line, hough_line_peaks)
import cv2
import matplotlib.pyplot as plt

"""# **Algorithm for canny edge detection**
1.Noise Reduction : It is used for the noise reduction from the image. For this it uses Gaussian filter (5*5).

1.Finding Intensity Gradient of the Image (Direction in which, intensity of the pixel value change drastically).

3.Non-maximum Suppression

4.Hysteresis Thresholding

# **Checking for rough image**
"""

img=cv2.imread("./Dataset/Rough/1.jpg",0)

img.shape

plt.imshow(img)
plt.show()

edges = cv2.Canny(img,45,100)

plt.imshow(edges)
plt.show()

# Generating various point
tested_angles = np.linspace(-np.pi/2, np.pi / 2, 360)

hspace, theta, dist = hough_line(edges, tested_angles)

hspace.shape, theta.shape, dist.shape

h, angle, distance = hough_line_peaks(hspace, theta, dist,num_peaks =10)

angles = [a*180/np.pi for a in angle]

angle_difference = np.max(angles) - np.min(angles)

np.max(angles),np.min(angles)

"""# **Ans**"""

print(angle_difference)

"""# **Checking for image2**"""

img=cv2.imread("./Dataset/4/clock_1.png",0)

edges = cv2.Canny(img,45,100)

plt.subplot(1,2,1)
plt.imshow(img)
plt.subplot(1,2,2)
plt.imshow(edges)
plt.show()

# Generating various point
tested_angles = np.linspace(-np.pi/2, np.pi / 2, 360)

hspace, theta, dist = hough_line(edges, tested_angles)

h, angle, distance = hough_line_peaks(hspace, theta, dist,num_peaks =10)

angles = [a*180/np.pi for a in angle]

angle_difference = np.max(angles) - np.min(angles)

"""# **Ans**"""

print(angle_difference)

"""# **Checking for image3**"""

img=cv2.imread("./Dataset/4/clock_2.jpg",0)

edges = cv2.Canny(img,45,100)

plt.subplot(1,2,1)
plt.imshow(img)
plt.subplot(1,2,2)
plt.imshow(edges)
plt.show()

# Generating various point
tested_angles = np.linspace(-np.pi/2, np.pi / 2, 360)

hspace, theta, dist = hough_line(edges, tested_angles)

h, angle, distance = hough_line_peaks(hspace, theta, dist,num_peaks =10)

angles = [a*180/np.pi for a in angle]

angle_difference = np.max(angles) - np.min(angles)

"""# **Ans**"""

print(angle_difference)

