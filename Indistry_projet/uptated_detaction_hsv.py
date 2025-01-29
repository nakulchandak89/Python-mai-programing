import cv2
import numpy as np

# Global variable to store the clicked coordinates
clicked_coordinates = None

# Function to handle mouse events
def mouse_callback(event, x, y, flags, param):
    global clicked_coordinates
    if event == cv2.EVENT_LBUTTONDOWN:
        # When left mouse button is clicked, store the coordinates
        clicked_coordinates = (x, y)
        print(f"Clicked at: ({x}, {y})")

# Function to detect and print HSV values from the clicked pixel
def detect_hsv_value(frame, coordinates):
    if coordinates is not None:
        # Convert the frame to HSV color space
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Get the HSV value of the clicked pixel
        h, s, v = hsv_frame[coordinates[1], coordinates[0]]
        print(f"HSV value at ({coordinates[0]}, {coordinates[1]}): ({h}, {s}, {v})")
        return (h, s, v)
    return None

# Load an image or capture from video
image = cv2.imread('Indistry_projet\\Resources\\images\\image.png')  # Change to your image path
# Alternatively, use video capture
# cap = cv2.VideoCapture("Indistry_projet\\Resources\\video\\Video_input_1.mp4")

# Create a window to display the image
cv2.namedWindow('Image')
cv2.setMouseCallback('Image', mouse_callback)

# Display the image and wait for a click event
while True:
    # Show the image
    cv2.imshow('Image', image)
    
    # If clicked coordinates are stored, detect HSV value at the clicked point
    if clicked_coordinates is not None:
        detect_hsv_value(image, clicked_coordinates)
        clicked_coordinates = None  # Reset after reading the value

    # Wait for the user to press the 'q' key to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
