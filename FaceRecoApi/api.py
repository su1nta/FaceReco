# import necessary packages
import cv2
import PIL.Image as pim
import dlib
import numpy as np
import face_recognition_models as frm

# load necessary face_recognition models
face_detector = dlib.get_frontal_face_detector()                        # face detector
face_landmark_model = frm.pose_predictor_model_location()
face_landmark_predictor = dlib.shape_predictor(face_landmark_model)     # 68-point face landmark detector
face_encoder_model = frm.face_recognition_model_location()
face_encoder = dlib.face_recognition_model_v1(face_encoder_model)       # 128D face encoder

# load the image file (PIL) and convert to RGB - not needed in this context
# def load_image_file(filename):
#     img = pim.Image.open(filename)
#     img = img.convert('RGB')
#     return np.asarray(img)


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


# get Euclidean distance of the known faces and detected faces (within a tolerance) - can be done in the compare_face function
# def face_distance(encoded_face, face_to_compare):
#     pass


# compare known faces and detected and encoded faces
def compare_faces(encoded_faces, known_encoded_faces):
    face_matches = []
    compare_distance = []
    known_index = []
    tolerance = 0.6
    for encoded_face in encoded_faces:
        compare_distance = np.linalg.norm(known_encoded_faces - encoded_face, axis=1)
        # print(compare_distance)
        
        temp = 0 
        index = 0
        for each in compare_distance:   
            if each <= tolerance:
                known_index.append(index)
                temp = 1
            index += 1
            # else:
            #     face_matches.append(False)
        if temp == 1:
            face_matches.append(True)
        else:
            face_matches.append(False)


    return face_matches,known_index

# mail unknown faces once to a specified email
def mail_unknown_faces(unknown_faces, index):
    """
    :param unknown_faces: the path where the unknown faces are stored
    :param index: index of the latest unknown face
    """
    pass
