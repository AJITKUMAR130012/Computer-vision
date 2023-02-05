**Assignment1:**

**Question1.** <br />
 1.Read the image.<br />
 2.Divide the image in equal part with respect to width by using slicing in equal part( Shape of image is (386, 700, 3) ). So now the shape becomes ((386, 350, 3) and (386, 350, 3)).<br />
 3.Take the X-OR of both images and then plot it.<br />
 4.Take the Difference of both images and then plot it.<br />
**Question2:**<br />
 1.Read the image.<br />
 2.Extract the text from the images and store inside the “result” variable.<br />
 3.Format of the output of the easy-ocr is:<br />                                                                                                                  [([[51, 5], [107, 5], [107, 19], [51, 19]], 'Tniikistal', 0.16009526434695096)]<br />
 4.Calculate the midpoint of state by traversing the list.<br />
 5.Finally calculate the euclidean distance between both coordinate.<br />
 
**Question3:**<br />
References: https://scikit-image.org/docs/stable/auto_examples/edges/plot_circular_elliptical_hough_transform.html<br />

 1.Read the image in BGR format.<br />
 2.Read the image in grayscale.<br />
 3.Detect the edge from the gray image.<br />
 4.Guess the radius from range.<br />
 5.Calculate all the circles for each point in the edge image(edge  image is calculated by canny edge detection method).<br />
 6.Then peaked the most prominent 1 circle among all the detected circles.<br />
 8.Then calculate the perimeter and area.<br />
 
References: https://www.geeksforgeeks.org/circle-detection-using-opencv-python/<br />

 1.Read the image.<br />
 2.Read the image in grayscale.<br />
 3.Blur the image to remove the noise if present.<br />
 4.Use opencv to detect all the circles present in the image(In opencv it first detects the edge and then detects the circle and for this it takes the parameter in function itself like min_radius,max_radius,min_threshold and max_threshold.<br />
 5.Draw the first circle which is detected.<br />
 6.At last calculate the area and perimeter.<br />

**Question4:**<br />
References:https://github.com/codespaces<br />
Algorithm:<br />

 1.Generate various line on the edge of line that is done by the canny edge.<br />
 2.Then find the “r” and “Ө” for each the line.<br />
 3.The line for which “r” and “Ө” is same at each point that line is main line.<br />
 4.So in that way, we will find the line and during the hough transformation, we have “Ө” value also.<br />
 5.So we will subtract the maximum and minimum angle to find the resultant angle.<br /><br />
 
**Question5:**<br />
 1.Three images downloaded from the given link in the question.<br />
 2.Read all the three images one by one and then append them into the list.<br /><br /><br />
 3.Resize all the three images by using opencv.<br /><br />
 4.Calculate the average of all the three images along x-axis.<br />
 5.Subtract the image2 from image1 and then show it.<br />
 6.Salt(White) noise adds into the dark region.<br />
 7.To add the 5% probability, we first calculate the 5% of total image size. And make the 5% position of total images to 255.<br />
 9.To remove the Salt noise, we use the median filter. Generally the median filter is used to remove the salt noise.<br />
 10.Construct a numpy array=[[−1, −1, −1], [0, 0, 0], [ 1, 1, 1]].<br /><br />
 11.Then use opencv, 2D filter to convolve over them.<br />
 
**Question6:**<br />
 1.Randomly selected 100 images of “0” and “1” and put them into the two separate folders.<br />
 2.Traverse each image of both folders and the folder which contain images of “0” only, give them label “0” and similarly “1” label to images containing “1”. Read all the images and compute the horizontal projection profile. Then flatten them and give the label according to the above rule.<br />
 3.Then I store all the images and label offline into a desktop using the pickle module in python.<br />
 4.Then read the module by loading them and read separately as feature and label.<br />
 5.Next divide into X_train,y_train,X_test,y_test.<br />
 6.Then apply the SVM classifier and KNN from the sk-learn and found the accuracy 100 percent on test data.<br />
 7.Then plot the result also to show the result by both classifiers.<br />

**Question7:**
References: https://docs.opencv.org/3.4/d4/d73/tutorial_py_contours_begin.html<br /><br />

 1.For Black text white background<br />
 2.Read the image.<br />
 3.Convert it into the gray scale.<br />
 4.Find the edge using a canny edge detection method.<br />
 5.Then find the contours. <br />
 6.And draw the contour on the coordinate that is found by the find contour method.<br />

**Question8:**<br />
References: <br />
https://docs.opencv.org/4.x/df/dfb/group__imgproc__object.html#gga3a7850640f1fe1f58fe91a2d7583695dac6677e2af5e0fae82cc5339bfaef5038<br />
 1.Read the image and the template( Image containing my name “Ajit” and template containing character “A”.<br />
 2.Resize the template to 256*256.<br />
 3.In template matching, we calculate the distance between template and image and take the region where the difference is minimum.<br />


 So minimize the expression:<br />

 ![Screenshot from 2023-01-29 16-04-50](https://user-images.githubusercontent.com/60688738/216811171-b7f0d92a-5428-43cd-935e-2d8f15ea2f89.png)

 Where f is the image and t is the template.<br />
 After expanding:<br />
 ![Screenshot from 2023-01-29 16-06-18](https://user-images.githubusercontent.com/60688738/216811181-5fe45edd-fc83-483b-b43b-9312f8f76aee.png)

 So generally, maximize the below expression and this is cross-correlation.<br />
 ![Screenshot from 2023-01-29 16-08-56](https://user-images.githubusercontent.com/60688738/216811198-524e8003-edd4-4d0b-9547-645169970f70.png)

 4.So for that we use opencv template matching function.<br />
 5.To suppress all the unwanted matching, we set the threshold value to 0.7.<br />
 6.Then calculate the location, where matching is above than threshold value.<br />
 7.Then draw a rectangle over the matched location.<br />
 
**Question9:**<br />
References: <br />
https://docs.opencv.org/3.4/d4/d1b/tutorial_histogram_equalization.html<br />

 1.Read the image.<br />
 2.Convert into the gray.<br />
 3.Using the opencv, write the code to histogram of pixel value with bin size.<br />
 **Way histogram plot shows the information:**<br />
    a.X-axis contains the gray value of the pixel and the y-axis denotes the number of pixels that have the given range.<br />
 4.Then by using opencv perform histogram equalization and observe that quality of image is enhanced.<br />
 **Algorithm for the Histogram Equalization:**<br />
   1.First find the number of pixels for each gray level in the image.<br />
   2.Then find the probability of each pixel of gray level.<br />
   3.Then find the PDF.<br />
   4.Then find the CDF by adding all the previous PDF.<br />
   5.Then multiply each CDF to the maximum gray value of the pixel.<br />
   6.Then convert each value to the integer.<br />
   
**Question10:**<br />
 1.Read both images.<br />
 2.Extract the text from both images and store into “Result1” and “Result2”.<br />
 3.Easyocr extract the text in format of <br />
      [([[51, 5], [107, 5], [107, 19], [51, 19]], 'Tniikistal', 0.16009526434695096)]<br />
 4.So by using the indexing and slicing, find the last three digits.<br />

