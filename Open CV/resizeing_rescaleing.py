#in this code i had done resizing of image and rescaleing of teh image and same we will do for video also 

import cv2

# img = cv2.imread(r"Open CV\\mix.png")

# cv2.imshow("img",img)


# #this function is for resizeing the image and rescaleing the image 
# def rescaleFrame (frame, scale=0.75): #75% of size is less now as scall is 0.75 so if we make it 0.10 it will be 10% of the og 
#     width = int(frame.shape[1]*scale) #width is define 
#     height = int (frame.shape[0]*scale) #height is define
    
#     demensions = (width,height) #demension is tuple variable for storing the data 

#     return cv2.resize(frame,demensions, interpolation=cv2.INTER_AREA)


# resize_image = rescaleFrame(img)
# cv2.imshow("new",resize_image)

# cv2.waitKey(0)

# cv2.destroyAllWindows()



#this code is for resizeing the video 
capture = cv2.VideoCapture(r"Open CV\\resources\\video.mp4")
#same function 
def rescaleFrame (frame, scale=0.80):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    demensions = (width,height)

    return cv2.resize(frame,demensions, interpolation=cv2.INTER_AREA)



while True:
    isTrue, frame = capture.read()
    frame_resize = rescaleFrame(frame) #function call and pass the argument 
    cv2.imshow("Video",frame) 
    cv2.imshow("new",frame_resize) #take the output of the function work

    if cv2.waitKey(20) & 0xFF==ord("k"):
        break

capture.release()
cv2.destroyAllWindows()
