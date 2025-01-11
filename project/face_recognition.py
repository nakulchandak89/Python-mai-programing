# script for face recognition 

import cv2
import numpy as np

video = cv2.VideoCapture(0)

while True:

    ret, video_data = video.read()
    video_data = cv2.flip(video_data, 1)
    cv2.imshow("Live Video",video_data)
    if cv2.waitKey(10) & 0xFF==ord("q"):
        break

video.release()
cv2.destroyAllWindows()
