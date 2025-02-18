'''
Problem Statement:
Write a program to detect edges in an image using the Canny edge detection technique. 
Then, find and draw all the contours present in the image. 
Finally, display the total number of contours detected.
'''


import cv2
import numpy 

img = cv2.imread("Open CV\\resources\leuvenB.jpg") #this is the path of the image
 
cv2.imshow("image", img) #get the og image 

blur = cv2.GaussianBlur(img, (5, 5), cv2.BORDER_DEFAULT) #we blure the image(image, (kernal size), Pixel extrapolation method for border handling.)
cv2.imshow("blus", blur) #display the image

canny = cv2.Canny(blur, 125, 255) #w apply canny for age dection 

contourm,hierarchy = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) #(image, mode, Method)
#cv2.RETR_LIST: Retrieves all the contours without creating a hierarchy.
#cv2.CHAIN_APPROX_SIMPLE: Compresses horizontal, vertical, and diagonal segments, leaving only their endpoints
cv2.drawContours(img, contourm, -1,(0,255,0), 2) #(og image, countours, countureIdx, color, Thickness)

cv2.imshow("final img", img)



cv2.waitKey(0)
cv2.destroyAllWindows()
