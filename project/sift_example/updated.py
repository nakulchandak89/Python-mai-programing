import cv2
import numpy as np

# Load the replacement image
replacement_image = cv2.imread('Open CV\\resources\\image.jpg')

# Start video feed
cap = cv2.VideoCapture(0)

# Minimum area threshold for major objects (adjust as needed)
min_area_threshold = 3100

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to HSV and define red color ranges
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # lower_red1 = np.array([0, 120, 70])
    # upper_red1 = np.array([10, 255, 255])
    # lower_red2 = np.array([170, 120, 70])
    # upper_red2 = np.array([180, 255, 255])
    # grean1 = np.array([35, 100, 100])
    # grean2 = np.array([85, 255, 255])
    black = np.array([125, 6, 255])
    black2 = np.array([124,13, 153])
    # Create masks for red color
    mask_black = cv2.inRange(hsv_frame, black, black2)
    # mask = cv2.inRange(hsv_frame,grean1, grean2)
    # mask1 = cv2.inRange(hsv_frame, lower_red1, upper_red1)
    # mask2 = cv2.inRange(hsv_frame, lower_red2, upper_red2)
    # red_mask = cv2.bitwise_or(mask1, mask2)

    # Find contours for the red regions
    contours, _ = cv2.findContours(mask_black, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Filter contours by area
        area = cv2.contourArea(contour)
        if area < min_area_threshold:
            continue  # Skip minor objects

        # Get the bounding box of the contour
        x, y, w, h = cv2.boundingRect(contour)

        # Resize the replacement image to fit the bounding box
        resized_replacement = cv2.resize(replacement_image, (w, h))

        # Create a mask for the detected shape
        shape_mask = np.zeros_like(frame, dtype=np.uint8)
        cv2.drawContours(shape_mask, [contour], -1, (255, 255, 255), thickness=cv2.FILLED)
        object_mask = cv2.inRange(shape_mask, (255, 255, 255), (255, 255, 255))
        resized_mask = object_mask[y:y+h, x:x+w]

        # Replace the detected region with the replacement image
        replacement_cropped = cv2.bitwise_and(resized_replacement, resized_replacement, mask=resized_mask)
        background = cv2.bitwise_and(frame[y:y+h, x:x+w], frame[y:y+h, x:x+w], mask=cv2.bitwise_not(resized_mask))
        result = cv2.add(background, replacement_cropped)
        frame[y:y+h, x:x+w] = result

    # Display the processed frame
    cv2.imshow('Red Object Detection', frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
