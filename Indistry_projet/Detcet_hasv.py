import cv2
import numpy as np

# Function to detect and print HSV values from the image
def detect_hsv_values(frame):
    # Convert the frame to HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Loop through each pixel in the image
    height, width, _ = hsv_frame.shape
    for y in range(height):
        for x in range(width):
            # Get the HSV value of the current pixel
            h, s, v = hsv_frame[y, x]
            
            # You can print or filter based on specific values
            print(f"Pixel at ({x},{y}) - HSV: ({h}, {s}, {v})")

            # If you want to detect a specific color, add a filter
            if 80 <= h <= 100 and 70 <= s <= 100 and 80 <= v <= 100:
                print(f"Detected Green at ({x}, {y}) - HSV: ({h}, {s}, {v})")

# Load an image or capture from video
image = cv2.imread('Indistry_projet\\Resources\\images\\image.png')  # Change to your image path
# Alternatively, use video capture
# # cap = cv2.VideoCapture("Indistry_projet\\Resources\\video\\Video_input_1.mp4")

# # Process the image or video frame
detect_hsv_values(image)

# Optionally, if you are using video, you can capture frames and process like this:
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#     detect_hsv_values(frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

cv2.destroyAllWindows()
