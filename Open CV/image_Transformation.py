#this code is for translocating teh image 
import cv2
import numpy as np

img = cv2.imread("Open CV\\resources\mix.png")
cv2.imshow("image",img)

# #function useed for translocating 
# def  translocation (img ,x, y):
 
#  transMat = np.float32([[1,0,x],[0,1,y]]) #Moves the image by x pixels along the x-axis and y pixels along the y-axis.
#  dimensions = (img.shape[1], img.shape[0]) #Ensures the output image is the same size as the input image.
#  return cv2.warpAffine(img,transMat,dimensions) #Applies the affine transformation using the translation matrix.


# translated = translocation(img,100,100)
# cv2.imshow("translocated",translated)


#dono code sath mai nahi chalte 
'''
note:-
-x --> Left
-y --> Up
x --> Right
y --> Down
'''

'''
The function rotate(img, angle, 
rotpoint=None) rotates an image by a specified angle around a given rotation point (rotpoint). 
If no rotation point is provided, it defaults to the center of the image.
'''
def rotate(img, angle, rotpoint=None):
 (height,width) = img.shape[:2]

 if rotpoint is None:
  rotpoint=(width//2,height//2) #this calculate the center  of the image 

  rotMat=cv2.getRotationMatrix2D(rotpoint,angle,1.0) #creates the transformation matrix for rotation 
  dimensions = (width,height)

  return cv2.warpAffine(img,rotMat,dimensions)
 
rotated = rotate(img,45)
cv2.imshow("rotated",rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()

'''
explanation of this 
def rotate(img, angle, rotpoint=None):
    """
    Rotates an image by a given angle around a specified rotation point.

    Parameters:
    img: np.ndarray
        The input image.
    angle: float
        The angle of rotation in degrees.
    rotpoint: tuple or None
        The point around which the image will be rotated (default: image center).

    Returns:
    np.ndarray
        The rotated image.
    """
    # Get the dimensions of the image (height and width)
    (height, width) = img.shape[:2]

    # If no rotation point is provided, default to the center of the image
    if rotpoint is None:
        rotpoint = (width // 2, height // 2)

    # Create the rotation matrix
    # rotpoint: Rotation center
    # angle: Rotation angle in degrees
    # 1.0: Scale (1.0 = no scaling)
    rotMat = cv2.getRotationMatrix2D(rotpoint, angle, 1.0)

    # Dimensions of the rotated image (same as the original image)
    dimensions = (width, height)

    # Perform the rotation using cv2.warpAffine and return the rotated image
    return cv2.warpAffine(img, rotMat, dimensions)


# Example usage:
# Load an image
img = cv2.imread("path/to/image.jpg")

# Rotate the image by 45 degrees
rotated = rotate(img, 45)

# Display the rotated image
cv2.imshow("Rotated Image", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''