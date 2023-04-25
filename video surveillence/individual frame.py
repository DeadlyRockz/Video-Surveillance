import cv2
import os

# Open the video file
video = cv2.VideoCapture("C:\\Users\\rjpra\\OneDrive\\Desktop\\New folder\\videos\\output.mp4")

# Create a directory to save the frames
output_dir = 'C:/Users/rjpra/OneDrive/Desktop/New folder/image/'
os.makedirs(output_dir, exist_ok=True)

# Initialize variables
frame_count = 0

# Loop through the video frames
while True:
    # Read a frame from the video
    ret, frame = video.read()

    # Break the loop if there are no more frames
    if not ret:
        break

    # Save the frame as an image with high quality
    output_file = os.path.join(output_dir, f'frame_{frame_count:04d}.jpg')
    cv2.imwrite(output_file, frame, [cv2.IMWRITE_JPEG_QUALITY, 100])

    # Increment the frame count
    frame_count += 1

# Release the video file
video.release()

