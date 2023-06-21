# import necessary packages
import PIL.Image as im
import dlib
import numpy as np
import PIL.ImageFile as imfile


# load the image file (PIL) and convert to RGB
def load_image_file(image):
    pass


# detect faces in an image
def detect_face(frame):
    pass


# detect facial landmarks in a detected face
def face_landmarks(detected_frame):
    pass


# encode the face
def face_encode(detected_frame, known_detected_frame=None):
    pass


# get Euclidean distance of the known faces and detected faces (within a tolerance)
def face_distance(encoded_face, face_to_compare):
    pass


# compare known faces and detected and encoded faces
def compare_faces(encoded_face, known_encoded_face):
    pass


# mail unknown faces once to a specified email
def mail_unknown_faces(unknown_faces):
    pass
