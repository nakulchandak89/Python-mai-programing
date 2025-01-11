#this is the syntax of thersholding 

import cv2
import numpy as np

img = cv2.imread("Open CV\\resources\cat1.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#simple Thresholding
#thresholding, thresh = cv2.threshold(src, thresh_value, max_value, threshold_type)
thresholding,thresh = cv2.threshold(gray,150,255, cv2.THRESH_BINARY) 
cv2.imshow("thresh1",thresh)

#addaptive thersholding 
#adaptive_thresholding = cv2.adaptiveThreshold(src, max_value, adaptive_method, threshold_type, block_size, C)
adaptive_thersholding =  cv2.adaptiveThreshold(gray,255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 5)
cv2.imshow("Adaptive", adaptive_thersholding)

 

cv2.waitKey(0)
cv2.destroyAllWindows()

#Code Breckdown 
'''
1)src: The source image, which must be a single-channel grayscale image (e.g., gray in your case).
2)The threshold value: Pixels with intensity values greater than or less than this value will be modified based on the threshold_type.
3)max_value: The value assigned to the output pixels when the condition specified by the threshold_type is met.
4)threshold_type: Determines the type of thresholding to apply. Common options include:
--> cv2.THRESH_BINARY
--> cv2.THRESH_BINARY_INV
--> cv2.THRESH_TRUNC
--> cv2.THRESH_TOZERO
--> cv2.THRESH_TOZERO_INV

*) adaptive Threshold
1) adaptive_method
--> cv2.ADAPTIVE_THRESH_MEAN_C
--> cv2.ADAPTIVE_THRESH_GAUSSIAN_C

'''
