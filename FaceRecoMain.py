import cv2 as cv
import  numpy as np
import FaceRecoApi as api
import os
import json

class NoKnownFaceException(Exception):
    pass

names = []
known_encoded_faces = []

# set font parameters
font = cv.FONT_HERSHEY_DUPLEX
font_scale = 0.6
font_color = (0, 0, 0)
font_thickness = 1

# get the path of known_faces.json file
current_directory = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(current_directory,'assets', 'known_faces.json')

with open(path, "r") as json_read:
        data = json.load(json_read)

# get the known names and encoded faces from known_faces.json
for item in data:
    for key,_ in item.items():
        if key == "Name":   
            names.append(item.get(key))
        else:
            known_encoded_faces.append(item.get(key))

# the process count - this is a check to process the faces in a frame
# after a specific iteration
process_count = 0
n = 5

# capturing from webcam
capture_face_from_webcam = True
capture = cv.VideoCapture(0)

while capture_face_from_webcam:
    process_this_frame = True
    while process_this_frame:
        #taking one frame at a time
        status, frame = capture.read()

        # flipping the frame horizontally
        flipped_frame = cv.flip(frame,1)

        # increase the process count
        process_count += 1

        # checking if we process this frame or not        
        if process_count % n == 0:    
            # resize the frame to 1/4th size for faster search preocess
            resized_frame = cv.resize(flipped_frame, (0, 0), fx = 1, fy = 1)

            # convert the image from BGR to RGB 
            rgb_image = cv.cvtColor(resized_frame, cv.COLOR_BGR2RGB)
            # convert the image from BGR to RGB 
            faces = api.detect_face(rgb_image)
            # print(faces)

            # if any face is detected
            if len(faces) > 0:
                # Detecting faces
                landmarks = api.face_landmarks(rgb_image, faces)

                # encoding faces and storing them encoded_faces list 
                encoded_faces = np.array(api.face_encode(rgb_image, landmarks))

                # Comparing faces
                face_matches = []
                known_faces_index = []
                face_matches,known_faces_index = api.compare_faces(encoded_faces,
                                                             known_encoded_faces)

                # a list containing indexes of matched faces
                matched_faces_indexes = []
                unmatched_faces_indexes = []

                # capture all the matched faces indices in a list
                index = 0
                for match in face_matches:
                    if match:
                        matched_faces_indexes.append(index)
                    elif not match:
                         unmatched_faces_indexes.append(index)
                    index += 1

                print("Any match : " , face_matches)
                print(matched_faces_indexes)

                # associate matched faces with names
                match_to_name = {}

                for index1, index2 in zip(matched_faces_indexes, known_faces_index):
                    match_to_name[index1] = names[index2]

                # show the matched faces and their names, unknown faces in the frame
                known_face = []
                unknown_face = []
                if len(matched_faces_indexes) > 0:
                    for index in matched_faces_indexes:
                        known_face = faces[index]
                        print("Known face: ", known_face)
                        cv.rectangle(flipped_frame, (known_face.left(), known_face.top()), 
                                    (known_face.right(), known_face.bottom()), 
                                    (0, 255, 0), 2)

                        if index1 in match_to_name:
                            name = match_to_name[index1]
                            cv.rectangle(flipped_frame, 
                                        (known_face.left(), known_face.bottom()),
                                        (known_face.right(), known_face.bottom() + 50),
                                        (0, 255, 0), cv.FILLED)
                            cv.putText(flipped_frame, name, (known_face.left() + 5, 
                                                            known_face.bottom() + 35), 
                                        font, font_scale, font_color, font_thickness)
                if len(unmatched_faces_indexes) > 0:
                    for index in unmatched_faces_indexes:
                        unknown_face = faces[index]
                        print("Unknown face: ", unknown_face)
                        cv.rectangle(flipped_frame,
                                    (unknown_face.left(), unknown_face.top()),
                                    (unknown_face.right(), unknown_face.bottom()), 
                                    (0, 0, 255), 2)

            process_this_frame = False

    # if the process iteration is complete reset the process count
    if process_count >= n:
        process_count = 0          

    # show the processed or unprocessed frame
    cv.imshow('Flipped Frame', flipped_frame)

    # if key 'q' is pressed it will stop capturing from the webcam
    if cv.waitKey(1) & 0xFF == ord('q'):
        capture_face_from_webcam = False

#end of capture
capture.release()
cv.destroyAllWindows()
