import face_recognition

# Load known faces from images
known_image = face_recognition.load_image_file("known_face.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

# Capture and process a new face for recognition
unknown_image = face_recognition.load_image_file("unknown_face.jpg")
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

# Compare face encodings
results = face_recognition.compare_faces([known_encoding], unknown_encoding)
if results[0]:
    print("Authentication successful - Face recognized!")
else:
    print("Authentication failed - Face not recognized.")

from pyfingerprint.pyfingerprint import PyFingerprint

# Initialize Fingerprint sensor
fingerprint = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

if not fingerprint.verifyPassword():
    raise ValueError('The given fingerprint sensor password is wrong!')

# Search for a fingerprint template
if fingerprint.readImage():
    fingerprint.convertImage(0x01)
    result = fingerprint.searchTemplate()

    if result == -1:
        print('Fingerprint not recognized!')
    else:
        print('Fingerprint recognized!')
else:
    print('Failed to read fingerprint image')
