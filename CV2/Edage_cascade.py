#this is the edage dectaction script
import cv2
import numpy as np

image = cv2.imread("Open CV\\resources\cat1.jpg")

cv2.imshow("og image", image)

blur = cv2.GaussianBlur(image, (5, 9), cv2.BORDER_DEFAULT) # This is the syntax for bluring the image 
cv2.imshow("Imag2", blur)

canny = cv2.Canny(blur, 125, 175) # this is the cannys Edage Cascade 

cv2.imshow("canny", canny)
cv2.waitKey(0)

cap = cv2.VideoCapture(0)

while True:
    istrue, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2.imshow("cap", frame)

    if cv2.waitKey(20) & 0xFF== ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

