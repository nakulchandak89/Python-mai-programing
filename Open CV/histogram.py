#we are creating the histogram on the saturation of pixels 

import cv2
import numpy as np
import matplotlib.pyplot as plt 

img =  cv2.imread("Open CV\\resources\cars.jpg")
cv2.imshow("cars",img)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)

gray_hist =  cv2.calcHist([gray],[0],None,[256],[0,256])

plt.figure()
plt.title("gray histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixcels")
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

cv2.waitKey(0)
cv2.destoryAllWindows()
