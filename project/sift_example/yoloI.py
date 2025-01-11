import cv2

# Path to your video
video_path = "project\Resources\\red news.mp4"

# Open the video file
cap = cv2.VideoCapture(video_path)
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Save every 50th frame
    if frame_count % 50 == 0:
        frame_path = f"dataset_frame_{frame_count}.jpg"
        cv2.imwrite(frame_path, frame)
        print(f"Saved: {frame_path}")

    frame_count += 1

# Release the video
cap.release()
print("Frame extraction completed.")


#work in progress
