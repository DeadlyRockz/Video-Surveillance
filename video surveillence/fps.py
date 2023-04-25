import cv2
import os

# Set the capture device, in this case, the default webcam
cap = cv2.VideoCapture(0)

# Set the video codec and FPS
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = 30

# Set the output directory
output_dir = 'C:\\Users\\rjpra\\OneDrive\\Desktop\\New folder\\videos'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Set the output file name
output_file = os.path.join(output_dir, 'output.mp4')

# Set the video writer
out = cv2.VideoWriter(output_file, fourcc, fps, (640, 480))

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret:
        # Write the frame into the video writer
        out.write(frame)

        # Display the resulting frame
        cv2.imshow('frame', frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything when finished
cap.release()
out.release()
cv2.destroyAllWindows()
