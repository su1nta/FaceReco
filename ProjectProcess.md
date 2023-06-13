### System Overview
- FaceRecoMain
    - import packages : openCV (cv2), numpy, FaceRecoApi
    - capture the face from webcam
    - load known face image locations (numpy array) and face encodings and store them in a function object list
    - initialize a variable to determine process this frame or not (process_this_frame = true)
    - read a frame from the capture. A frame is a still image from the video
    - if the frame will be processed:
        - resize the frame to 1/4th size for faster search preocess
        - convert the image from BGR to RGB (Not sure if useful or not)
        - genetate face locations: find the face (numpy array) and face encodings from the current frame
        - compare the found faces with known faces
            - retrieve the name if the face is recognized
    - set process this frame to false : stop processing the frame anymore
    - 
- FaceRecoApi
    -


###  Important Videos for concept clearing
- Python functions are first class objects and can be assigned to another object/variable
    - for example there is a following code: 
    ```
    detector = dlib.get_frontal_face_detector()
    # here get_frontal_face_detector is a function which reference is passed to the object detector. Now detector is a function object which is like a pointer to
    # the function get_frontal_face_detector()
    ```
    - here is a [video](https://www.youtube.com/watch?v=p8RU0JH2xb8) explained why python functions are first class objects

- What is a HOG classification/model? [video link here](https://www.youtube.com/watch?v=thcB1NcorV8)

