# import required packages
import dlib
import cv2

# import the image
img = cv2.imread('example.jpg')
img_resized = cv2.resize(img, (0, 0), fx=0.50, fy=0.50)

# initialize face detector
detector = dlib.get_frontal_face_detector()

# detect faces from an image
faces = detector(img_resized, 0)
print(type(faces))

# convert face from dlib rect to plain tuple
face_tuple = ()
for face in faces:
    face_tuple = (face.top(), face.right(), face.bottom(), face.left())
print(face_tuple)


# detect face landmarks

