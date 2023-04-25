import cv2

# Load the object detection model
model = cv2.dnn.readNetFromTensorflow('frozen_inference_graph.pb', 'ssd_mobilenet_v2_coco_2018_03_29.pbtxt')

# Open the video file
cap = cv2.VideoCapture('test_video.mp4')

# Set the video codec
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# Get the video dimensions
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create an output video writer
out = cv2.VideoWriter('output_video.mp4', fourcc, 30.0, (width, height))

# Loop over frames from the video
while cap.isOpened():
    # Read a frame from the video
    ret, frame = cap.read()

    if not ret:
        break

    # Run object detection on the frame
    model.setInput(cv2.dnn.blobFromImage(frame, size=(300, 300), swapRB=True, crop=False))
    detections = model.forward()

    # Loop over the detected objects
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:
            class_id = int(detections[0, 0, i, 1])
            x1 = int(detections[0, 0, i, 3] * width)
            y1 = int(detections[0, 0, i, 4] * height)
            x2 = int(detections[0, 0, i, 5] * width)
            y2 = int(detections[0, 0, i, 6] * height)

            # Draw a bounding box around the object
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Write the frame to the output video
    out.write(frame)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Exit if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video file and the output video writer
cap.release()
out.release()

# Destroy all windows
cv2.destroyAllWindows()
