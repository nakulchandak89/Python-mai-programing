# Bitwise opration used in open cv 

import cv2 
import numpy as np

blank = np.zeros((500,500),dtype="uint8")


rectangle = cv2.rectangle(blank.copy(), (30,30),(470,470),255,thickness=-1)
circle = cv2.circle(blank.copy(),(250,250),250,255,thickness=-1)

cv2.imshow("rectangle",rectangle)
cv2.imshow("circle",circle)

#bitwise AND it shades the comman area of both the shapes 
Bitwise_and = cv2.bitwise_and(rectangle,circle)
cv2.imshow("And",Bitwise_and)

#bitwsie_or it impose both the shapes 
bitwise_or = cv2.bitwise_or(rectangle, circle)
cv2.imshow("Or",bitwise_or)

#nitwise XOR it shades the uncomman part of both the shapes 
bitwise_xor = cv2.bitwise_xor(rectangle,circle)
cv2.imshow("XOR",bitwise_xor)

#bitwise NOT (it basicaly return the inverting value of the given curve and we need to pass only one shape at once )
bitwise_not = cv2.bitwise_not(rectangle)
cv2.imshow("NOT",bitwise_not)



cv2.waitKey(0)
cv2.destroyALLWindows()



