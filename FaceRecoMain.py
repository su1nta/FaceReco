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

# the process count - this is a check to process the faces in a frame
# after a specific iteration
process_count = 0
n = 15

# set the named window
window_name = 'FaceReco'
cv.namedWindow(window_name, cv.WINDOW_NORMAL)

# set desired window size
window_width = 640
window_height = 480
cv.resizeWindow(window_name, window_width, window_height)

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
            detected_faces = api.detect_face(rgb_image)
            # print(faces)

            # if any face is detected
            if len(detected_faces) > 0:
                # Detecting faces
                landmarks = api.face_landmarks(rgb_image, detected_faces)

                # encoding faces and storing them encoded_faces list 
                encoded_faces = np.array(api.face_encode(rgb_image, landmarks))

                # Comparing faces
                face_matches = []
                known_faces_index = []
                matched_faces,unmatched_faces, unmatched_encodings = api.compare_faces(detected_faces,
                                                                encoded_faces)

                # show the matched faces and their names, unknown faces in the frame
                known_face = []
                unknown_face = []
                if len(matched_faces) > 0:
                    for matched_name, matched_face in matched_faces.items():
                        known_name = matched_name
                        known_face = matched_face
                        cv.rectangle(flipped_frame, 
                                    (known_face.left(), known_face.top()), 
                                    (known_face.right(), known_face.bottom()), 
                                    (0, 255, 0), 2)
                        cv.rectangle(flipped_frame, 
                                    (known_face.left(), known_face.bottom()),
                                    (known_face.right(), known_face.bottom() + 50),
                                    (0, 255, 0), cv.FILLED)
                        cv.putText(flipped_frame, known_name, (known_face.left() + 5, 
                                                        known_face.bottom() + 35), 
                                    font, font_scale, font_color, font_thickness)
                elif len(unmatched_faces) > 0:
                    api.process_unknown_faces(flipped_frame, unmatched_faces, unmatched_encodings)
                    for unknown_face in unmatched_faces:
                        cv.rectangle(flipped_frame,
                                    (unknown_face.left(), unknown_face.top()),
                                    (unknown_face.right(), unknown_face.bottom()), 
                                    (0, 0, 255), 2)
                else:
                    for face in detected_faces:
                        cv.rectangle(flipped_frame, (face.left(), face.top()), 
                                        (face.right(), face.bottom()), 
                                        (255, 0, 0), 2)
                        cv.rectangle(flipped_frame, 
                                            (face.left(), face.bottom()),
                                            (face.right(), face.bottom() + 50),
                                            (255, 0, 0), cv.FILLED)
                        cv.putText(flipped_frame, 'No Face Added', (face.left() + 5, 
                                                                face.bottom() + 35), 
                                            font, font_scale, (255,255,255),
                                            font_thickness)

            process_this_frame = False

    # if the process iteration is complete reset the process count
    if process_count >= n:
        process_count = 0          

    # show the processed or unprocessed frame
    cv.imshow(window_name, flipped_frame)

    # if key 'q' is pressed it will stop capturing from the webcam
    if cv.waitKey(1) & 0xFF == ord('q'):
        capture_face_from_webcam = False

#end of capture
capture.release()
cv.destroyAllWindows()
