# import necessary packages
import os
import cv2
import PIL.Image as pim
import dlib
import numpy as np
import json
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
def compare_faces(detected_faces, encoded_faces):

    """
        :param: detected_faces and encoded_faces
        :return: matched_faces and unmatched_faces

        - known_encoded_faces is a dictionary of known_faces.json file
        - this function will process the encoded faces from known encodings
        - dictionary and list names are self explanatory
    """

    # deserialize data from json file
    known_encoded_faces = {}
    current_directory = os.path.dirname(os.path.abspath('__file__'))
    path = os.path.join(current_directory,'assets', 'known_faces.json')
    with open(path, "r") as json_read:
        known_encoded_faces = json.load(json_read)

    # dictionary and list which will contain matched and unmatched faces
    matched_faces = {}
    unmatched_faces = []

    # list which will contain euclidean distance between
    # a detected face and known encoded faces
    compare_distance = []

    # tolerance - how much distance measure will be tolerated
    tolerance = 0.6

    index = 0
    for encoded_face in encoded_faces:
        temp = 0
        fetched_name = ""
        if len(known_encoded_faces) > 0:
            for face in known_encoded_faces:
                fetched_name = face.get('Name')
                encoding = face.get('Encoding')
                compare_distance = np.linalg.norm(encoded_face - encoding, axis=0)

                if compare_distance <= tolerance:
                    temp = 1
                    break

            if temp == 1:       # matched faces found
                print("fetched name: ",fetched_name)
                matched_faces[fetched_name] = detected_faces[index]
            else:
                unmatched_faces.append(detected_faces[index])
        index += 1

    return matched_faces, unmatched_faces


# mail unknown faces once to a specified email
def mail_unknown_faces(unknown_faces, index):
    """
    :param unknown_faces: the path where the unknown faces are stored
    :param index: index of the latest unknown face
    """
    pass
