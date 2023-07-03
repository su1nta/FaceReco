# import required packages
import dlib
import cv2
import face_recognition_models

# note: OpenCV uses BGR color scheme by default to process images,
# whereas dlib uses RGB, so they are converted as needed to process faces properly

# import the image
img = cv2.imread('example.jpg')

print("img type: ", type(img))

# resize the image to half of it's size
img_resized = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)

print("img_resized type: ", type(img_resized))

# convert image from BGR to RGB
img_rgb = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)

print("img_rgb type: ", type(img_rgb))

# initialize face detector
detector = dlib.get_frontal_face_detector()

# detect faces from an image
faces = detector(img_rgb, 1)


# Draw rectangles on the image
for face in faces:
    cv2.rectangle(img_rgb, (face.left(), face.top()), (face.right(), face.bottom()), (0, 255, 0), 2)


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

# print no. of detected faces in the image
text = "Detected faces: " + str(len(faces))
# set font parameters
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
font_scale = 0.7
font_color = (0, 0, 0)
font_thickness = 1

# set image coordinates
img_width, _, _ = img_rgb.shape
text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)
text_width, _ = text_size
text_position = (10, img_width - 10)

cv2.rectangle(img_rgb, (2, img_width - 30), (text_width + 15, img_width), (255, 255, 255), thickness=cv2.FILLED)
cv2.putText(img_rgb, text, text_position, font, font_scale, font_color, font_thickness)

# convert RGB image back to BGR
img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)

# display the image in the window
cv2.imshow('Face Landmark', img_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
