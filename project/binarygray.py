import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the image
image = cv2.imread('Open CV\\resources\mix.png')

# # Create a mask
# mask = np.zeros(image.shape, dtype="uint8")
# cv2.rectangle(mask, (50, 50), (200, 200), 255, -1)  # Mask a rectangular region

# # Apply the mask
# masked_image = cv2.bitwise_and(image, image, mask=mask)

# # Calculate histogram for masked region
# hist = cv2.calcHist([image], [0], mask, [256], [0, 256])

# # Display the images and histogram
# cv2.imshow("Original Image", image)
# cv2.imshow("Masked Image", masked_image)

# plt.plot(hist)
# plt.title("Histogram for Masked Image")
# plt.xlabel("Pixel Intensity")
# plt.ylabel("Frequency")
# plt.show()




# Split the channels
channels = cv2.split(image)
colors = ('b', 'g', 'r')
plt.title("Color Image Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")

# Calculate and plot histogram for each channel
for channel, color in zip(channels, colors):
    hist = cv2.calcHist([channel], [0], None, [256], [0, 256])
    plt.plot(hist, color=color)

plt.legend(colors)
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()
