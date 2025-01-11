#in this code we are going to drow an shape on image and also creating an blank image 

import cv2
import numpy as np

#this method is using numpy 
blank = np.zeros((500,500,3),dtype="uint8") #this is an blank image dtype is an data type uint8 which is for image
# 500,500 is hight and width of an blank image  
cv2.imshow("Blank",blank) #we print the blank image 

#now from this blank image we will fill some color to it 
# blank[:] = 0,255,0 # for Green color 
# cv2.imshow("Green",blank)

# #now we wil get color to pixels and shape will be sqare and remaining area will be of green as it came first 
# blank[200:300, 300:400] = 255,0,0  # for Blue Color
# cv2.imshow("blue",blank)

# blank[:] = 0,0,225 #for red color
# cv2.imshow("Red",blank)

# blank[:] = 100,100,100 #this is an example of Color palet, We can make color creation 
# cv2.imshow("Mix",blank)

#this is to make an rectangle for this we need to pass argument in this way cv2.rectangle(img,pt1,pt2,color,thickness)
# cv2.rectangle(blank,(0,0),(250,500),(0,255,0),thickness=cv2.FILLED)  #in this we can change coordanets eg:-(0,0),(250,500) we will note a big change
# cv2.imshow("Rectangle",blank)

# #this is syntax for making the circle :- cv2.circle(img,(center),(radius),(color),thickness)
# cv2.circle(blank,(250,250),100,(0,0,255),thickness=-1)
# cv2.imshow("Circle",blank)

#for line cv2.line(blank,pt1,pt2,color,thickness)
# cv2.line(blank,(250,250),(250,500),(255,0,0),thickness=3)
# cv2.imshow("Line",blank)

#for writing the text syntax is cv2.putText(image, text, org, fontFace, fontScale, color, thickness, lineType)
cv2.putText(blank,"Hello World",(225,225), cv2.FONT_HERSHEY_COMPLEX,1.0,(0,0,255), 2)
cv2.imshow("Text",blank)


cv2.waitKey(0)
cv2.destroyAllWindows()

'''
# In this code, we are going to draw shapes on an image and create a blank image.

import cv2
import numpy as np

# Step 1: Create a blank image using NumPy
# `np.zeros()` creates an array filled with zeros, which represents a black image.
# The shape (500, 500, 3) means the image has a height and width of 500 pixels, 
# and 3 color channels (for RGB).
# `dtype="uint8"` specifies the data type for pixel values, where uint8 (unsigned 8-bit integer) is standard for images.
blank = np.zeros((500, 500, 3), dtype="uint8")  

# Display the blank (black) image
cv2.imshow("Blank", blank)  

# Step 2: Fill the blank image with a specific color (Green in this case)
# `blank[:] = 0, 255, 0` sets all pixels in the image to the color Green.
# The format is BGR (Blue, Green, Red), where (0, 255, 0) means maximum Green, no Red, and no Blue.
blank[:] = 0, 255, 0  
cv2.imshow("Green", blank)  

# Step 3: Draw a smaller square of Blue color on the green image
# `blank[200:300, 300:400] = 255, 0, 0` changes the pixel values in the region
# defined by rows 200-300 and columns 300-400 to Blue.
# This creates a square of Blue color within the larger Green area.
blank[200:300, 300:400] = 255, 0, 0  
cv2.imshow("Blue", blank)  

# Step 4: Fill the entire image with Red color
# `blank[:] = 0, 0, 225` changes all pixels to Red.
# The BGR format (0, 0, 225) represents maximum Red, no Green, and no Blue.
blank[:] = 0, 0, 225  
cv2.imshow("Red", blank)  

# Step 5: Experiment with custom colors
# `blank[:] = 100, 100, 100` sets the entire image to a custom grayish color.
# You can use this technique to create any color by adjusting the BGR values.
blank[:] = 100, 100, 100  
cv2.imshow("Mix", blank)  

# Wait for the user to press a key
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()

'''