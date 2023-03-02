# -*- coding: utf-8 -*-
"""Computer_vision_Assignment1_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NhroULOxb22HOQuUe2DqwO59r6T-KN23
"""

!git clone https://github.com/AJITKUMAR130012/Computer-vision.git

cd Computer-vision

!ls

cd Assignment1

!ls

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

img=cv2.imread("./Dataset/1/Spot_the_difference.png",1)

plt.imshow(img)
plt.show()

img.shape

img1=img[:,:350]
img2=img[:,350:]

img1.shape, img2.shape

plt.subplot(1, 2,1)
plt.imshow(img1)
#plt.show()
plt.subplot(1, 2,2)
plt.imshow(img2)
plt.show()

"""#By using the X-or operation"""

xor_img = cv2.bitwise_xor(img1,img2)

plt.imshow(xor_img)
plt.show()

"""# By using the difference Operator"""

diff_img=img1-img2

plt.imshow(diff_img)
plt.show()
