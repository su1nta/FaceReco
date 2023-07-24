# import necessary packages
import dlib
import cv2
import numpy as np
import face_recognition_models

# load and resize two images
img1 = cv2.imread('compare2.jpg')
img2 = cv2.imread('compare22.jpg')

# img1_resized = cv2.resize(img1, (0, 0), fx=0.5, fy=0.5)
# img2_resized = cv2.resize(img2, (0, 0), fx=0.5, fy=0.5)

# change the image from BGR to RGB
img1_rgb = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2_rgb = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

# load face detector and detect images
detector = dlib.get_frontal_face_detector()
faces1 = detector(img1_rgb, 1)
faces2 = detector(img2_rgb, 1)

# find landmarks
predictor_model = face_recognition_models.pose_predictor_model_location()
predictor = dlib.shape_predictor(predictor_model)

landmarks1 = []
landmarks2 = []

for face in faces1:
    face_landmarks = predictor(img1_rgb, face)
    landmarks1.append(face_landmarks)

for face in faces2:
    face_landmarks = predictor(img2_rgb, face)
    landmarks2.append(face_landmarks)

# encode the faces
encoder_model = face_recognition_models.face_recognition_model_location()
encoder = dlib.face_recognition_model_v1(encoder_model)

encoding1 = []
encoding2 = []

encoded_face1_np = []
encoded_face2_np = []

for landmark in landmarks1:
    encoded_face1 = encoder.compute_face_descriptor(img1_rgb, landmark, 1)
    encoded_face1_np = np.array(encoded_face1)

for landmark in landmarks2:
    encoded_face2 = encoder.compute_face_descriptor(img2_rgb, landmark, 1)
    encoded_face2_np = np.array(encoded_face2)

# compare the faces
same_face = False
tolerance = 0.5

# compare = encoding1 - encoding2
# axis = 0  because there is only one face to compare with
compare_float = np.linalg.norm(encoded_face1_np - encoded_face2_np)
if compare_float <= tolerance:
    same_face = True

# print no. of detected faces in the image
text = "Same Face: " + str(same_face)
print(text)
# set font parameters
font = cv2.FONT_HERSHEY_DUPLEX
font_scale = 0.6
font_color = (0, 0, 0)
font_thickness = 1

# set image coordinates
img1_width, _, _ = img1_rgb.shape


# put if faces matches
for face in faces1:
    cv2.rectangle(img1_rgb, (face.left(), face.top()), (face.right(), face.bottom()), (0, 255, 0), 2)
    cv2.rectangle(img1_rgb, (face.left(), face.bottom()), (face.right(), face.bottom() + 50), (0, 255, 0), cv2.FILLED)
    cv2.putText(img1_rgb, text, (face.left() + 5, face.bottom() + 35), font, font_scale, font_color, font_thickness)

# convert RGB image back to BGR
img_bgr = cv2.cvtColor(img1_rgb, cv2.COLOR_RGB2BGR)

# display the image in the window
cv2.namedWindow("Face Landmark", cv2.WINDOW_KEEPRATIO)
cv2.imshow('Face Landmark', img_bgr)
if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()
