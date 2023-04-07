import numpy as np
import cv2
import math
import time
import matplotlib.lines as mlines
import matplotlib.pyplot as plt
start_time = time.time()


# Load the image
path="./Dataset/Problem-2/line2.png"
img = cv2.imread(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edge_image = cv2.GaussianBlur(gray, (3, 3), 1) 

# Set the threshold for detecting edges
edge_image = cv2.Canny(edge_image, 50, 150, apertureSize=3)
edge_image = cv2.dilate(
        edge_image,
        cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)),
        iterations=1
    )
edge_image = cv2.erode(
        edge_image,
        cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)),
        iterations=1
    )
# cv2.imshow("edge", edge_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

figure = plt.figure(figsize=(12, 12))
subplot1 = figure.add_subplot(1, 3, 1)
subplot1.imshow(img)
subplot2 = figure.add_subplot(1, 3, 2)
subplot2.imshow(edge_image, cmap="gray")
subplot3 = figure.add_subplot(1, 3, 3)
subplot3.imshow(img)

# Set the Hough Transform parameters
rho_resolution = 1
theta_resolution = np.pi / 180
threshold = 250
height,width=edge_image.shape
lines = cv2.HoughLines(edge_image, rho_resolution, theta_resolution, threshold, None, 0, 0)
white_img = np.ones((width, height), dtype = np.uint8)
if lines is not None:
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
            pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
            #cv2.line(white_img, pt1, pt2, (0,0,255), 3, cv2.LINE_AA)
            subplot3.add_line(mlines.Line2D([pt1[0], pt2[0]], [pt1[1], pt2[1]]))

end_time=time.time()
print(end_time-start_time)
subplot1.title.set_text("Original Image")
subplot2.title.set_text("Edge Image")
subplot3.title.set_text("Detected_lines")

plt.show()

# cv2.imshow("Detected Lines", white_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()