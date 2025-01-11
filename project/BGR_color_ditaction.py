# code for detacting 3 basic color from images 
#logic converted the image to hsv and masked ot with the range of all the three basic color 


#this code is to detact red color form the providrd image
import cv2 
import numpy as np

img = cv2.imread(r"Open CV\\resources\windows logo.jpeg")
cv2.imshow("Og image ",img)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# cv2.imshow("hsv",hsv)

lower_red1=np.array([0,50,50]) #upper red values 
upper_red1=np.array([10,255,255])
lower_red2=np.array([170,50,50]) #lower red values 
upper_red2=np.array([180,255,255])
#chack the imaeg range
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv,lower_red2, upper_red2)

red_mask = mask1 + mask2 

result = cv2.bitwise_and(img,img,mask=red_mask)
# cv2.imshow("red mask image",red_mask) 

cv2.imshow("final output",result) # detacted image of red color from image 

#form hear teh code is for detacting teh Blue color from the image 
lower_blue2 = np.array([90,50,50]) #lower range of blue  this value of blue is for sky blue 
upper_blue2 = np.array([110,255,255]) #upper range of blue  (for dark blue we should change the values to 110 to 130 )

mask2 = cv2.inRange(hsv, lower_blue2, upper_blue2)
# cv2.imshow("blue",mask2) #blue masked image 

result = cv2.bitwise_and(img, img, mask=mask2) 

cv2.imshow("result", result) #resulting image of detacted blue color

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_green = np.array([35,50,50])
upper_green = np.array([85,255,255])

mask  = cv2.inRange(hsv, lower_green, upper_green)
result = cv2.bitwise_and(img,img, mask=mask)

cv2.imshow("gree",result)



cv2.waitKey(0)
cv2.destroyAllWindows()



