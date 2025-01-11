# import cv2
# import numpy as np

# sift = cv2.SIFT_create()
# # Load an image
# image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# # Detect keypoints and descriptors
# keypoints, descriptors = sift.detectAndCompute(image, None)

# print(f"Number of keypoints detected: {len(keypoints)}")
# # Draw keypoints on the image
# output_image = cv2.drawKeypoints(image, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# # Display the image
# cv2.imshow('SIFT Keypoints', output_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
# matches = bf.match(descriptors1, descriptors2)

# # Sort matches by distance
# matches = sorted(matches, key=lambda x: x.distance)

# # Draw matches
# matched_image = cv2.drawMatches(img1, keypoints1, img2, keypoints2, matches[:50], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# cv2.imshow('Matches', matched_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import numpy as np

# Load two images
img1 = cv2.imread('Open CV\\resources\image.jpg', cv2.IMREAD_GRAYSCALE)  # Query image
img2 = cv2.imread('Open CV\\resources\mix.png', cv2.IMREAD_GRAYSCALE)  # Train image

# Check if images are loaded properly
if img1 is None or img2 is None:
    print("Error loading images!")
    exit()

# Create SIFT detector
sift = cv2.SIFT_create()

# Detect keypoints and compute descriptors
keypoints1, descriptors1 = sift.detectAndCompute(img1, None)
keypoints2, descriptors2 = sift.detectAndCompute(img2, None)

# Print number of keypoints detected
print(f"Keypoints in image1: {len(keypoints1)}")
print(f"Keypoints in image2: {len(keypoints2)}")

# Use BFMatcher for feature matching
bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
matches = bf.match(descriptors1, descriptors2)

# Sort matches by distance
matches = sorted(matches, key=lambda x: x.distance)

# Draw top 50 matches
matched_image = cv2.drawMatches(img1, keypoints1, img2, keypoints2, matches[:50], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# Display the result
cv2.imshow('SIFT Keypoint Matches', matched_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
