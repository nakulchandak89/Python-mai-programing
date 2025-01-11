# Edge Detaction basic syntax

import cv2
import numpy as np

img = cv2.imread("Open CV\\resources\cat1.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#lapLaction 
lap = cv2.Laplacian(gray, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))

# cv2.imshow("lap",lap)
#sobel
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 1)
sobely = cv2.Sobel(gray, cv2.CV_64F, 1, 0)

cv2.imshow("Sobel x", sobelx)
cv2.imshow("sobel y", sobely)

cv2.waitKey(0)
cv2.destroyAllWindows()
