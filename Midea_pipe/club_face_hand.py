#this is the script is club is face and hand detaction scripts 
import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
mphands = mp.solutions.hands  # Load Mediapipe's Hands solution
hands = mphands.Hands()  # Create an instance of the Hands class for processing
mpDraw = mp.solutions.drawing_utils 
mpFace = mp.solutions.face_detection
mpdraw = mp.solutions.drawing_utils
facedetection = mpFace.FaceDetection()

while True:
    isTrue, frame = cap.read()
    frame = cv2.flip(frame, 1)
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert the BGR image to RGB (required by Mediapipe)

    # Process the frame to detect hands
    result = hands.process(imgRGB)  # Analyze the frame for hand landmarks

    # Check if any hands are detected
    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:  # Loop through each detected hand
            # Draw the hand landmarks and connections on the frame
            mpDraw.draw_landmarks(frame, handLms, mphands.HAND_CONNECTIONS)
    result = facedetection.process(imgRGB)
    if result.detections:
        for id, detection in enumerate(result.detections):
            mpdraw.draw_detection(frame, detection)


    cv2.imshow("cam", frame)
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
