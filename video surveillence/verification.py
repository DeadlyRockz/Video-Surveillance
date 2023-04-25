import os
import face_recognition

# Path to directory containing images
image_dir = "d:\\image"

# Load known face encodings
known_face_encodings = []
known_face_names = []
for file_name in os.listdir(image_dir):
    if file_name.endswith(".jpg") or file_name.endswith(".png"):
        image_path = os.path.join(image_dir, file_name)
        name = os.path.splitext(file_name)[0]
        image = face_recognition.load_image_file(image_path)
        face_encodings = face_recognition.face_encodings(image)
        if len(face_encodings) > 0:
            known_face_encodings.append(face_encodings[0])
            known_face_names.append(name)

# Load test image
test_image = face_recognition.load_image_file("D:\\image\\")

# Find faces in test image
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

# Compare face encodings to known faces
for face_encoding in face_encodings:
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    name = "Unknown"
    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]
    print(f"Found face of {name} in test image")
