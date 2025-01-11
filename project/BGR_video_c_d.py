# detacting the color from video as input

import cv2
import numpy as np

color_ranges = {
    "red" :(np.array([0,120,70]), np.array([10,255,255])),
    "green":(np.array([35,100,100]), np.array([85,255,255])),
    "blue":(np.array([100,150,0]),np.array([140,255,255]))
}

# video_path = ""
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: unable to open video")
    exit()

while True:
    ret,frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (640, 480))

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    for color_name, (lower, upper) in color_ranges.items():
        mask = cv2.inRange(hsv_frame, lower, upper)
        result = cv2.bitwise_and(frame,frame,mask=mask)

        cv2.imshow(f"{color_name} Detaction", result)

    cv2.imshow("og",frame)


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()





