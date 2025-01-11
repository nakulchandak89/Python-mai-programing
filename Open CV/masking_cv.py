#Masking of an image is shown in this code 

import cv2
import numpy as np

img = cv2.imread("Open CV\\resources\cars.jpg")
cv2.imshow("cars",img)

blank = np.zeros(img.shape[:2],dtype="uint8")
# cv2.imshow("Blank",blank)

mask = cv2.rectangle(blank,(250,250),(50,50),255,-1)
# cv2.imshow("Mask",mask)

masked = cv2.bitwise_and(img,img,mask=mask)
cv2.imshow("Mask image",masked)


cv2.waitKey(0)
cv2.destroyAllWindows()


#uint8 data type in known as


#this is also an method for masking 
# mask = cv2.circle(blank, (img.shape[1]//2,img.shape[0]//2),100,255,-1)