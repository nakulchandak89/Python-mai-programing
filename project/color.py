import cv2
import numpy as np

# Define HSV color ranges for detection
color_ranges = {
    "red": (np.array([0, 120, 70]), np.array([10, 255, 255])),
    "green": (np.array([35, 100, 100]), np.array([85, 255, 255])),
    "blue": (np.array([100, 150, 0]), np.array([140, 255, 255])),
}

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Unable to access webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to read frame.")
        break

    # Resize frame (optional, for better performance)
    frame = cv2.resize(frame, (640, 480))

    # Convert frame to HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Iterate over defined colors
    for color_name, (lower, upper) in color_ranges.items():
        mask = cv2.inRange(hsv_frame, lower, upper)  # Create mask for the color

        # Find contours for detected areas
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour) > 500:  # Ignore small areas (noise)
                x, y, w, h = cv2.boundingRect(contour)  # Get bounding box
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw rectangle
                cv2.putText(frame, f"{color_name.capitalize()}", (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)  # Label the box

    # Display the processed frame
    cv2.imshow("Live Color Detection with Boxes", frame)

    # Break the loop on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam and close all windows
cap.release()
cv2.destroyAllWindows()




# import cv2
# import numpy as np

# img  = cv2.imread("Open CV\windows logo.jpeg")
# cv2.imshow("green", img)



# cv2.waitKey(0)
# cv2.destroyAllWindows()
