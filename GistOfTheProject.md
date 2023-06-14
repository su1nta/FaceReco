# Gist of the project

## Libraries to Learn

### OpenCV

- [Tutorial to OpenCV](https://www.youtube.com/watch?v=oXlwWbU8l2o)
- OpenCV is a library of programming functions mainly for real-time computer vision

### Numpy

- [Numpy tutorial for beginners](https://www.youtube.com/watch?v=QUT1VHiLmmI)
- NumPy offers comprehensive mathematical functions, random number generators, linear algebra routines, Fourier transforms, and more

### Dlib

- C++ toolkit mainly used in this project for detection of 68 facial points (eye, nose, lips etc)
- [this medium blog is a good reference](https://towardsdatascience.com/facial-mapping-landmarks-with-dlib-python-160abcf7d672)

### Python Image Library (used modules in this project: Image and Imagefile)

- [Tutorial to Pillow](https://www.youtube.com/watch?v=5QR-dG68eNE)
- The Python Imaging Library adds image processing capabilities to your Python interpreter
- This library provides extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities
- The core image library is designed for fast access to data stored in a few basic pixel formats. It should provide a solid foundation for a general image processing tool

---

## System Overview

There is the main two program which will have the necessary functions to perform the face recognition
: FaceRecoMain (The main program) and FaceRecoApi (A module that contains the necessary functions)

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
    - Display the results : if the face is detected and recognized or not
      - draw a rectangle around the face
      - display a label with a name if the face is recognized
      - display the resulting image in the webcam
      - if exit key is pressed, exit from the loop
    - release the capture
    - destroy the resulting window

- FaceRecoApi
  - import packages: Python Image Library(PIL), dlib, numpy, trained face recognition models
  - load the image file
  - detect faces in the image
  - detect face features: eye, nose, lips, chin etc
  - encode the face: 128-dimension face encoding
  - get euclidean distance of the detected face and known faces
  - compare by distance and return list with distances and name if face is matched

---

## Models used to recognize faces

- import face_recognition_models
- face_recognition_model_location()
  - dlib_face_recognition_resent_model_v1.dat
- pose_predictor_five_point_model_location()
  - shape_predictor_5_face_landmarks.dat
- pose_predictor_model_location
  - shape_predictor_68_face_landmarks

---

## Important Videos and Blogs for concept clearing

- Python functions are first class objects and can be assigned to another object/variable
  - for example there is a following code: 

```python
    detector = dlib.get_frontal_face_detector()
    # here get_frontal_face_detector is a function which reference is passed to the object detector. Now detector is a function object which is like a pointer to the function get_frontal_face_detector()
```

  - here is a [video](https://www.youtube.com/watch?v=p8RU0JH2xb8) explained why python functions are first class objects
  - What is a HOG classification/model? [video link here](https://www.youtube.com/watch?v=thcB1NcorV8)

- Here is a medium blog from our main reference repo where the basics of face recognition is explained in brief but enough detailed manner
  - [Modern Face Recognition with Deep Learning](https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78)