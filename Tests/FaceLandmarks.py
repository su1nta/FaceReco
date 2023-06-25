# import required packages
import dlib
import cv2
import face_recognition_models

# import the image
img = cv2.imread('example.jpg')

print("img type: ", type(img))

# resize the image to half of it's size
img_resized = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)

print("img_resized type: ", type(img_resized))

# convert image from BGR to RGB
img_rgb = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)

print("img_rgb type: ", type(img_rgb))

# initialize face detector
detector = dlib.get_frontal_face_detector()

# detect faces from an image
faces = detector(img_rgb, 2)


# Draw rectangles on the image
for face in faces:
    cv2.rectangle(img_rgb, (face.left(), face.top()), (face.right(), face.bottom()), (0, 255, 0), 2)


# # convert face from dlib rect to plain tuple - not needed in this case
# face_tuple = ()
# for face in faces:
#     face_tuple = (face.top(), face.right(), face.bottom(), face.left())
# print(face_tuple)


# initialize the 68 point face predictor
predictor_model = face_recognition_models.pose_predictor_model_location()
predictor = dlib.shape_predictor(predictor_model)


# detect face landmarks
landmarks = []
for face in faces:
    face_landmarks = predictor(img_rgb, face)
    landmarks.append(face_landmarks.parts())


# this code is for multi-face prediction
for landmark in landmarks:
    for point in landmark:
        x = point.x
        y = point.y
        # place the landmark coordinate in the image using OpenCV
        cv2.circle(img_rgb, (x, y), 1, (0, 0, 255), -1)


# convert RGB image back to BGR
img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)

# display the image in the window
cv2.imshow('Face Landmark', img_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()