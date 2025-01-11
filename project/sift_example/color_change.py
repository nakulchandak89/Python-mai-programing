import cv2
import numpy as np

# Load the main image
image = cv2.imread("project\Resources\later_frame_4.jpg")

# Load the replacement image
replacement_image = cv2.imread('Open CV\\resources\image.jpg')

# Convert to HSV and define the red color range
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])

# Create masks for red color
mask1 = cv2.inRange(hsv_image, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv_image, lower_red2, upper_red2)
red_mask = cv2.bitwise_or(mask1, mask2)

# Find contours for the red regions
contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Minimum area threshold for major objects
min_area_threshold = 3000  # Adjust this as needed

# Loop through detected contours
for contour in contours:
    # Filter contours by area
    area = cv2.contourArea(contour)
    if area < min_area_threshold:
        continue  # Skip minor objects

    # Create a blank mask for the detected shape
    shape_mask = np.zeros_like(image, dtype=np.uint8)

    # Draw the contour as a filled shape on the mask
    cv2.drawContours(shape_mask, [contour], -1, (255, 255, 255), thickness=cv2.FILLED)

    # Isolate the detected region in the original image
    object_mask = cv2.inRange(shape_mask, (255, 255, 255), (255, 255, 255))

    # Get the bounding box of the contour to resize the replacement image
    x, y, w, h = cv2.boundingRect(contour)
    resized_replacement = cv2.resize(replacement_image, (w, h))

    # Create a mask for the resized replacement image
    resized_mask = object_mask[y:y+h, x:x+w]

    # Overlay the replacement image on the original image
    # 1. Keep only the masked region of the resized replacement
    replacement_cropped = cv2.bitwise_and(resized_replacement, resized_replacement, mask=resized_mask)

    # 2. Remove the detected region from the original image
    background = cv2.bitwise_and(image[y:y+h, x:x+w], image[y:y+h, x:x+w], mask=cv2.bitwise_not(resized_mask))

    # 3. Combine the background and the cropped replacement
    result = cv2.add(background, replacement_cropped)

    # 4. Place the result back in the original image
    image[y:y+h, x:x+w] = result

# Show the result
cv2.imshow('Shape-Fitted Replacement (No Black Frame)', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
