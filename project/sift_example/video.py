import cv2
import numpy as np

# Load replacement image
replacement_image = cv2.imread('project\Resources\Proper .jpg')

# Start video feed
cap = cv2.VideoCapture(0)

# Minimum area threshold for contours
min_area_threshold = 3000
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    if not ret:
        break

    # Preprocessing
    frame = cv2.convertScaleAbs(frame, alpha=1.5, beta=20)
    frame = cv2.GaussianBlur(frame, (5, 5), 0)

    # Convert to HSV and define red ranges
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    # Create red mask
    mask1 = cv2.inRange(hsv_frame, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv_frame, lower_red2, upper_red2)
    red_mask = cv2.bitwise_or(mask1, mask2)

    # Find contours
    contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw all contours for debugging
    debug_frame = frame.copy()
    cv2.drawContours(debug_frame, contours, -1, (0, 255, 0), 2)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area < min_area_threshold:
            continue  # Skip small objects

        # Draw bounding box for debugging
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(debug_frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Resize replacement image
        resized_replacement = cv2.resize(replacement_image, (w, h))

        # Create mask for the shape
        shape_mask = np.zeros_like(frame, dtype=np.uint8)
        cv2.drawContours(shape_mask, [contour], -1, (255, 255, 255), thickness=cv2.FILLED)
        object_mask = cv2.inRange(shape_mask, (255, 255, 255), (255, 255, 255))
        resized_mask = object_mask[y:y+h, x:x+w]

        # Replace region
        replacement_cropped = cv2.bitwise_and(resized_replacement, resized_replacement, mask=resized_mask)
        background = cv2.bitwise_and(frame[y:y+h, x:x+w], frame[y:y+h, x:x+w], mask=cv2.bitwise_not(resized_mask))
        result = cv2.add(background, replacement_cropped)
        frame[y:y+h, x:x+w] = result

    # Debugging outputs
    cv2.imshow('Original Frame', frame)
    cv2.imshow('Red Mask', red_mask)
    cv2.imshow('Contours Debug', debug_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
