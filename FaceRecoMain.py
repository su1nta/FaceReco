import cv2 as cv
import  numpy as np
import FaceRecoApi as api
import sys
import os
import json
import time as t


names = []
known_encoded_faces = []

# set font parameters
font = cv.FONT_HERSHEY_DUPLEX
font_scale = 0.6
font_color = (0, 0, 0)
font_thickness = 1



# capturing from webcam

current_directory = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(current_directory,'assets', 'known_faces.json')

with open(path, "r") as json_read:
        data = json.load(json_read)

if len(data) == 0:
        print("No known faces")
for item in data:
    for key,_ in item.items():
        if key == "Name":   
            names.append(item.get(key))
        else:
            known_encoded_faces.append(item.get(key))

# for item in  known_encoded_faces:
#     print(item)


capture_face_from_webcam = True

capture = cv.VideoCapture(0)
while capture_face_from_webcam:
    process_this_frame = True
    while process_this_frame:
        #taking one frame at a time
        status, frame = capture.read()
        # print(frame)
        # if not status:
        #     print()
        #     break
        
        # flipping the frame horizontally
        flipped_frame = cv.flip(frame,1)
        
        # resize the frame to 1/4th size for faster search preocess
        resized_frame = cv.resize(flipped_frame, (0, 0), fx = 1, fy = 1)

        # convert the image from BGR to RGB 
        rgb_image = cv.cvtColor(resized_frame, cv.COLOR_BGR2RGB)
        # convert the image from BGR to RGB 
        faces = api.detect_face(rgb_image)
        # print(faces)

        # Detecting faces
        landmarks = api.face_landmarks(rgb_image, faces)
        # print(landmarks)
        # encoding faces and storing them encoded_faces list 
        encoded_faces = np.array(api.face_encode(rgb_image, landmarks))

        # Comparing faces
        face_matches,known_index = api.compare_faces(encoded_faces,known_encoded_faces)

        matched_faces_indexes = []

        index = 0
        for match in face_matches:
            if match == True:
                
                matched_faces_indexes.append(index)
            index += 1
            
            


        print(matched_faces_indexes)
    
        # print(matched_faces_indexes)
        for index1 in matched_faces_indexes:
            face = faces[index1]
            cv.rectangle(flipped_frame, (face.left(),face.top()), (face.right(),face.bottom()), (255, 0, 0), 2)
        # for index2 in known_index:
        #     print(index2)
        #     name = names[index2]
        #     # cv.rectangle(flipped_frame, (face.left(), face.bottom()), (face.right(), face.bottom() + 50), (0, 255, 0), cv.FILLED)
            # cv.putText(flipped_frame, name, (face.left() + 5, face.bottom() + 35), font, font_scale, font_color, font_thickness)
        
        process_this_frame = False
        # end of processing image
    print("Any match : " , face_matches)

    # t.sleep(3)
    cv.imshow('Flipped Frame', flipped_frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        capture_face_from_webcam = False
        process_this_frame = False
    #end of capture
capture.release()
cv.destroyAllWindows()


            

