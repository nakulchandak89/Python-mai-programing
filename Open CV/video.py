import cv2

# Path to the video file
video_path = r"Open CV\\resources\\video2.mp4"  

# Open the video file
cap = cv2.VideoCapture(video_path)

# Check if the video was opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
else:
    # Get FPS (Frames per second) of the video
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Frames per second (FPS): {fps}")
    print(f"Total frames in video: {total_frames}")

    # Read and display the video frames
    frame_count = 0
    while True:
        ret, frame = cap.read()

        # Print the ret status to debug frame reading
        print(f"Reading frame {frame_count + 1}: {'Success' if ret else 'Failed'}")
        
        if not ret:
            print("Error reading frame or video has ended.")
            break

        # Display the frame
        cv2.imshow('Video', frame)

        # Wait for 1 millisecond and check if the user presses 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        frame_count += 1

    print(f"Processed {frame_count} frames.")

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
