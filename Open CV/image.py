
import tensorflow_hub as hub
import tensorflow as tf
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Load pre-trained MobileNetV2-SSD model from TensorFlow Hub
# Instead of using tf.saved_model.load(), use hub.load()
model = hub.load('https://tfhub.dev/tensorflow/ssd_mobilenet_v2/fpnlite_320x320/1') 

# The rest of your code remains the same...
category_index = {
    1: {'id': 1, 'name': 'person'},
    2: {'id': 2, 'name': 'bicycle'},
    3: {'id': 3, 'name': 'car'},
    4: {'id': 4, 'name': 'motorcycle'},
    5: {'id': 5, 'name': 'airplane'},
    # Add more classes from the dataset you want to detect
}

# Load the image
image_path = 'Open CV\\resources\cars.jpg'  # Provide the path to your image
image_np = np.array(cv2.imread(image_path))

# Convert the image to RGB
image_rgb = cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB)

# Expand dimensions for batch size of 1
input_tensor = tf.convert_to_tensor(image_rgb)
input_tensor = input_tensor[tf.newaxis,...]

# Run detection
output_dict = model(input_tensor)

# The output contains:
# 1. 'num_detections' -> Number of detected objects
# 2. 'detection_boxes' -> Bounding boxes of detected objects
# 3. 'detection_classes' -> Class IDs of detected objects
# 4. 'detection_scores' -> Confidence scores for each detection

# Get the results
num_detections = int(output_dict['num_detections'])
boxes = output_dict['detection_boxes'][0].numpy()
classes = output_dict['detection_classes'][0].numpy().astype(np.int32)
scores = output_dict['detection_scores'][0].numpy()

# Filter results based on a threshold (e.g., confidence > 0.5)
threshold = 0.5
filtered_boxes = []
filtered_classes = []
filtered_scores = []

for i in range(num_detections):
    if scores[i] > threshold:
        filtered_boxes.append(boxes[i])
        filtered_classes.append(classes[i])
        filtered_scores.append(scores[i])

# Draw the bounding boxes on the image
image_with_boxes = image_np.copy()
for i in range(len(filtered_boxes)):
    box = filtered_boxes[i]
    class_id = filtered_classes[i]
    score = filtered_scores[i]

    # Convert box coordinates from normalized to pixel values
    (ymin, xmin, ymax, xmax) = box
    (left, right, top, bottom) = (xmin * image_np.shape[1], xmax * image_np.shape[1],
                                  ymin * image_np.shape[0], ymax * image_np.shape[0])

    # Draw the bounding box and label
    label = category_index.get(class_id, {}).get('name', 'Unknown')
    color = (0, 255, 0)  # Green for bounding box

    # Draw rectangle
    cv2.rectangle(image_with_boxes, (int(left), int(top)), (int(right), int(bottom)), color, 2)
    
    # Add label
    label_text = f"{label}: {score:.2f}"
    cv2.putText(image_with_boxes, label_text, (int(left), int(top) - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

# Display the image with bounding boxes
plt.imshow(cv2.cvtColor(image_with_boxes, cv2.COLOR_BGR2RGB))
plt.axis('off')  # Hide axis
plt.show()
