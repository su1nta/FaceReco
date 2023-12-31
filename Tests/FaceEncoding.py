# import required packages
import dlib
import cv2
import face_recognition_models
# import Tests.FaceLandmarks      # face landmark detection is already tested in this file

# load the images
img = cv2.imread('example.jpg')

# resize the image
img_resized = cv2.resize(img, (0, 0), fx=0.50, fy=0.50)

# convert from BGR to RGB

img_rgb = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)

# load face detector
detector = dlib.get_frontal_face_detector()

# detect faces in the image
faces = detector(img_rgb, 1)

# load landmark predictor
predictor_model = face_recognition_models.pose_predictor_model_location()
predictor = dlib.shape_predictor(predictor_model)

# predict face landmarks
landmarks = []
for face in faces:
    face_landmarks = predictor(img_rgb, face)
    # face_landmarks.parts() is useful if we want to draw the points(facial landmarks) on the face image
    # the encoder needs the whole object_detection object (without the points list), so the whole object is added as a landmark element
    landmarks.append(face_landmarks)

# load face encoder
face_recognition_model = face_recognition_models.face_recognition_model_location()
face_encoder = dlib.face_recognition_model_v1(face_recognition_model)

# encode the faces
encodings = []
for landmark in landmarks:
    print(type(landmark))
    encoded_face = face_encoder.compute_face_descriptor(img_rgb, landmark, 1)
    encodings.append(encoded_face)
