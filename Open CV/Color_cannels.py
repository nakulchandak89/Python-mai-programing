#this code will have ouput for getting the output of differnt collor invove in image 
import cv2
import numpy as np

img = cv2.imread("Open CV\\resources\RGB.jpg")
cv2.imshow("RGB",img)
#we split the color in this and store in 3 differnt variable 
b,g,r = cv2.split(img)
#this will diffrently show the image contains diffrent color 
cv2.imshow("Blue",b)
cv2.imshow("Green",g)
cv2.imshow("Red",r)
#print the Array which contains the Pixels for the color containg 
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()
#the End of the code 