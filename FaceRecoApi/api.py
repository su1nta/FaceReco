# import necessary packages
import cv2
import PIL.Image as pim
import dlib
import numpy as np
import face_recognition_models as frm

# custom exceptions
class NoKnownFaceException(Exception):
    pass

# load necessary face_recognition models

# face detector
face_detector = dlib.get_frontal_face_detector()
face_landmark_model = frm.pose_predictor_model_location()

# 68-point face landmark detector
face_landmark_predictor = dlib.shape_predictor(face_landmark_model)

# 128D face encoder
face_encoder_model = frm.face_recognition_model_location()
face_encoder = dlib.face_recognition_model_v1(face_encoder_model)

# detect faces in an image
def detect_face(frame):
    faces = face_detector(frame, 1)
    return faces


# detect facial landmarks in a detected face
def face_landmarks(frame, faces):
    landmarks = []
    for face in faces:
        face_landmarks = face_landmark_predictor(frame, face)
        landmarks.append(face_landmarks)

    return landmarks


# encode the face
def face_encode(frame, landmarks):
    encoded_faces = []
    for landmark in landmarks:
        encoded_face = face_encoder.compute_face_descriptor(frame, landmark, 1)
        encoded_faces.append(encoded_face)

    return encoded_faces

# compare known faces and detected and encoded faces
def compare_faces(encoded_faces, known_encoded_faces):
    # list which will contain if the detected face is known or not
    face_matches = []

    # list which will contain euclidean distance between
    # a detected face and known encoded faces
    compare_distance = []

    # index of the known face in the known_faces.json file
    known_faces_index = []
    # tolerance - how much distance measure will be tolerated
    tolerance = 0.6

    for encoded_face in encoded_faces:
        if len(known_encoded_faces) > 0:
            compare_distance = np.linalg.norm(encoded_face - known_encoded_faces, axis=1)
        # else:
        #     raise NoKnownFaceException("No Known Faces Found to compare")
        
        temp = 0 
        index = 0
        if len(compare_distance) > 0:
            for each in compare_distance:   
                if each <= tolerance:
                    known_faces_index.append(index)
                    temp = 1
                index += 1
                # else:
                #     face_matches.append(False)
            if temp == 1:
                face_matches.append(True)
            else:
                face_matches.append(False)

    return face_matches,known_faces_index


# mail unknown faces once to a specified email
def mail_unknown_faces(unknown_faces, index):
    """
    :param unknown_faces: the path where the unknown faces are stored
    :param index: index of the latest unknown face
    """
    pass
