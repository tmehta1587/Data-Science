

import numpy as np 
import pandas as pd

import cv2
import matplotlib.pyplot as plt

emptyImg = np.zeros(shape=(512, 512, 3), dtype=np.uint8)

plt.imshow(emptyImg)

cv2.circle(emptyImg ,center=(100,100), radius=50, color=(0, 0, 255), thickness=5)

cv2.rectangle(emptyImg, pt1=(180,200), pt2=(280,300), color=(255, 0, 0), thickness=-1)

cv2.rectangle(emptyImg, pt1=(350, 20), pt2=(480,150), color=(0, 255, 0), thickness=5)

cv2.circle(emptyImg ,center=(380,400), radius=50, color=(0, 0, 255), thickness=-1)


cv2.line(emptyImg, pt1=(0, 0), pt2=(500, 500), color=(255,255,255), thickness=5)

cv2.imshow("Shapes", emptyImg)
cv2.waitKey(0)
cv2.destroyAllWindows()