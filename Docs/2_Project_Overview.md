# Project Overview
There is the main two program which will have the necessary functions to perform the face recognition
: FaceRecoMain (The main program) and FaceRecoApi (A module that contains the necessary functions)

- **FaceRecoMain**
  - Import necessary packages : 
    - Installed packages:
        - OpenCV (cv2) 
        - Numpy
        - OS
    - From the project
        - FaceRecoApi
  - capture the face from webcam
  - initialize a variable to determine process this frame or not
  - read a frame from the capture. A frame is a still image from the video
  - if the frame will be processed:
    - resize the frame to 1/4th size for faster search preocess
    - convert the image from BGR to RGB
    - genetate face locations: find the face (numpy array) and face encodings from the current frame
      - detect face
      - find face landmarks 
      - encode the face
    - compare the found faces with known faces
    - retrieve the name if the face is recognized
    - set process this frame to false : stop processing the frame anymore
    - Display the results : if the face is detected and recognized or not
      - draw a rectangle around the face
      - display a label with a name if the face is recognized
      - display the resulting image in the webcam
      - if exit key is pressed, exit from the loop
    - release the capture
    - destroy the resulting window

- **FaceRecoApi**
  - Import necessary packages 
    - Dlib
    - Numpy
    - OpenCV (cv2)
    - Python Image Library (PIL)
    - OS
    - Json
    - face_recognition_models
  - load the image file
  - detect faces in the image
  - detect face features: eye, nose, lips, chin etc
  - encode the face: 128-dimension face encoding
  - get euclidean distance of the detected face and known faces
  - compare by distance and return list with distances and name if face is matched
  - e-mail the unrecognized faces to a specific e-mail id once
    - there will be a separate directory to identify the unknown faces so no resending the same unknown face
      - identify unknown faces:
        - the face comparision(compare_faces) returns a list containing if the face is recognized or not(true or false)
        - faces that are not recognized will remain in the same index position as the face detection list
        - the unknown face will be cropped from the original image with the help of coordinates found on the face detection list
        - then the cropped new image will be sent as email
  - Add and Delete faces
    - two json files containing objects which will have: (*filenames:* `known_faces.json` and `unknown_faces.json`)
      - known_faces.json - contains a list of objects, where an object contains:
        - name of the person
        - the image encoding
      - unknown_faces.json - contains a list of objects, where an object contains:
        - the image encoding of the unknown person
---
