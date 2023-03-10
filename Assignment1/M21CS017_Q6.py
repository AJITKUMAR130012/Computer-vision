# -*- coding: utf-8 -*-
"""Computer_vision_Assignment1_6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YLGsTSXruJ2JzTL3hHYxGsx5kqQzgjZm
"""

!git clone https://github.com/AJITKUMAR130012/Computer-vision

cd Computer-vision

cd Assignment1

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import glob
import matplotlib.pyplot as plt
import cv2
import pickle
import random
from sklearn.model_selection import train_test_split
from sklearn.neighbors import NearestNeighbors
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import r2_score,accuracy_score

# Nearest neighbour and svm

#!pwd

#%cd Computer-vision/

#!ls

def project_profile_horizontal(thresh1):
    #thresh1=cv2.resize(thresh1,(256,256))
#      for i in range(28):
#         for j in range(28):
#             if thresh1[i][j]==0:
#                 thresh1[i][j]=1
#             elif thresh1[i][j]==255:
#                 thresh1[i][j]=0
    thresh1[thresh1==0]=1
    thresh1[thresh1==255]=0
    horizontal_projection = np.sum(thresh1, axis = 1)
    return horizontal_projection

dir = "./Dataset/6"
cv_img = []
categories=['0','1']
for category in categories:
    path=os.path.join(dir,category)
    label=categories.index(category)
    for img in os.listdir(path):
        img_path=os.path.join(path,img)
        # Reading the image in grayscale
        digit_img=cv2.imread(img_path,0)
        #print(img.shape)
        # converting the image to binary image
#         plt.imshow(digit_img)
#         break
        ret, thresh1 = cv2.threshold(digit_img, 120, 255, cv2.THRESH_BINARY)
        #plt.imshow(img)
        # project profile horizontal
#         plt.imshow(thresh1)
#         plt.show()
        #performing the projection_profile
        thres1=project_profile_horizontal(thresh1)
        thresh1=np.array(digit_img).flatten()
        cv_img.append([thresh1,label])
#     break

len(cv_img)

pick_in=open('data.pickle','wb')
pickle.dump(cv_img,pick_in)
pick_in.close()

pick_in=open('data.pickle','rb')
data=pickle.load(pick_in)
pick_in.close()

random.shuffle(data)
features=[]
labels=[]
for feature, label in data:
    features.append(feature)
    labels.append(label)

X_train,X_test,y_train,y_test= train_test_split(features,labels)

X_train

"""# SVM classifier"""

svc=SVC(C=1,kernel='poly',gamma='auto')

svc.fit(X_train,y_train)

pred_svc=svc.predict(X_test)

r2_score(pred_svc,y_test)

accuracy_score(pred_svc,y_test)

pred_svc

X_test[0].shape

l=np.array(X_test[0])
l = np.reshape(l, (28, 28))
print(pred_svc[0])
plt.imshow(l)
plt.show()

l=np.array(X_test[1])
l = np.reshape(l, (28, 28))
print(pred_svc[1])
plt.imshow(l)
plt.show()

print(pred_svc[2])
l=np.array(X_test[2])
l=np.reshape(l,(28,28))
plt.imshow(l)
plt.show()

knn=KNeighborsClassifier(3)

knn.fit(X_train,y_train)

pred_knn=knn.predict(X_test)

pred_knn

r2_score(pred_knn,y_test)

falg=False
for i in range(len(pred_knn)):
  if pred_knn[i]!=pred_svc[i]:
    flag=True
    print("No! prediction value of both classifier are different")
if falg==False:
  print("YES! Both predicted same")

l=np.array(X_test[0])
l = np.reshape(l, (28, 28))
print(pred_knn[0])
plt.imshow(l)
plt.show()

l=np.array(X_test[1])
l = np.reshape(l, (28, 28))
print(pred_knn[1])
plt.imshow(l)
plt.show()

l=np.array(X_test[2])
l = np.reshape(l, (28, 28))
print(pred_knn[2])
plt.imshow(l)
plt.show()

