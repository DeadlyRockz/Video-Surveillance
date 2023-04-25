import face_recognition

# Load the input image
image = face_recognition.load_image_file("C:\\Users\\rjpra\\OneDrive\\Desktop\\New folder\\image")

# Get the list of face encodings in the image
face_encodings = face_recognition.face_encodings(image)

# Check if any faces are detected in the image
if len(face_encodings) == 0:
    print("No faces found in the input image.")
else:
    # Get the first face encoding in the list
    first_face_encoding = face_encodings[0]

    # Print the first 128 elements of the first face encoding
    print(first_face_encoding[:128])
