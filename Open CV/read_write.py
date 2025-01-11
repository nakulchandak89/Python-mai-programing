#In this code we are going to write code for both video and photo to read them 
#chack the path of image and video 
import cv2 
# img = cv2.imread("Open CV\cat1.jpg")

# cv2.imshow("cat",img)

# cv2.waitKey(0)

# cv2.destroyAllWindows()

# capture = cv2.VideoCapture(r"Open CV\\video2.mp4")

# while True:
#     isTrue, frame = capture.read()  #this loop is important and enshure to get our video done 
#     cv2.imshow("video",frame)

#     if cv2.waitKey(20) & 0xFF==ord("k"):
#         break

# capture.release() # Releases the camera resource so it can be used by other programs.
# cv2.destroyAllWindow() #cv2.destroyAllWindow is the method to close all the windows open by the open cv 


#this code will flip the cam output as non inverting image 

capture = cv2.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    frame = cv2.flip(frame, 1)
    cv2.imshow("CAM",frame)

    if cv2.waitKey(20) & 0xFF==ord("k"):
        break

capture.release()
cv2.destroyAllWindows()


#now in this i had completed 2 task 1 is to read the images and second is to read the live foutage from cam
