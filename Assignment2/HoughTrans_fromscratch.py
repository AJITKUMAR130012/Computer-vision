import numpy as np
import cv2
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

# Set the Hough Transform parameters


figure = plt.figure(figsize=(12, 12))
subplot1 = figure.add_subplot(1, 3, 1)
subplot1.imshow(img)
subplot2 = figure.add_subplot(1, 3, 2)
subplot2.imshow(edge_image, cmap="gray")
subplot3 = figure.add_subplot(1, 3, 3)
subplot3.imshow(img)




rho_resolution = 1
theta_resolution = np.pi / 180
threshold = 250

# Define the Hough accumulator array
height, width = edge_image.shape
max_rho = np.ceil(np.sqrt(height**2 + width**2))
accumulator = np.zeros((int(max_rho*2/rho_resolution), int(180/theta_resolution)))
 
# Loop over all edge pixels
for y in range(height):
    for x in range(width):
        if edge_image[y,x] > 0:
            # For each edge pixel, loop over all possible lines
            for theta_index in range(len(accumulator[0])):
                theta = theta_index * theta_resolution
                rho = x * np.cos(theta) + y * np.sin(theta)
                rho_index = int((rho + max_rho) / rho_resolution)
                accumulator[rho_index, theta_index] += 1

# Find the indices of the lines that pass the threshold
rho_indices, theta_indices = np.where(accumulator > threshold)

# Draw the lines on the original image
for i in range(len(rho_indices)):
    rho = (rho_indices[i] - max_rho) * rho_resolution
    theta = theta_indices[i] * theta_resolution
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    subplot3.add_line(mlines.Line2D([x1, x2], [y1, y2]))

# Show the image with detected lines
end_time=time.time()
print(end_time-start_time)
subplot1.title.set_text("Original Image")
subplot2.title.set_text("Edge Image")
subplot3.title.set_text("Detected_lines")
plt.show()

# cv2.imshow("Detected Lines", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()