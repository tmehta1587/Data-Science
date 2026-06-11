
import cv2
import numpy as np

img = cv2.imread("shapes.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


_, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)

contours, hierachy = cv2.findContours(thresh, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    area = cv2.contourArea(cnt)
    if area < 100:
        continue

    if area > 100000:
        continue

    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arclength(cnt, True),True)

    n = len(approx)

    if n == 6:
        print("We have a hexgaon here")
        cv2.drawContours(img, [cnt], 0, (255,0,255),3)

    elif n == 3: 
        print("We have found a triangle")
        cv2.drawCountors(img, [cnt],0,(0,255,0),3)

    elif n>9:
        print("We found a circle")
        cv2.drawCountor(img, [cnt], 0,(0, 255, 0),3)

    elif n == 4:
        x, y, w, h = cv2.boundingReact(approx)
        aspect_ratio = float(w) / h
        if 0.95 <= aspect_ratio <= 1.05:
            print("We found a square")
            cv2.drawCountors(img, [cnt], 0, (255, 255, 0), 3)
        else: 
            print("We found a rectangle")
            cv2.drawCountours(img, [cnt], 0, (255, 0, 0), 3)

cv2.imshow("Detected Shapes", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

