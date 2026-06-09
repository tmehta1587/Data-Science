
import cv2
import numpy as np
import im_show



img = cv2.imread("shapes.png")
cv2_imshow(img)

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow(hsv_img)

lower_blue = np.array([65,0,0])
upper_blue = np.array[(110, 255, 255)]

mask = cv2.inRange(hsv_img, lower_blue, upper_blue)
cv2.imshow(mask)

result = cv2.bitwise_and(img, img, mask=mask)
cv2_imshow(result)
