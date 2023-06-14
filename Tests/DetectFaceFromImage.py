import dlib
import cv2

# Load the image
image = cv2.imread('biden.jpg')

# Initialize the face detector
detector = dlib.get_frontal_face_detector()

# Detect all faces in the image
face_rects = detector(image, 0)
name = "Joe Biden"
# Draw each rectangle on the image
for rect in face_rects:
    cv2.rectangle(image, (rect.left(),rect.top()), (rect.right(),rect.bottom()), (255,0,0), 2)

# Display the image with detected faces
cv2.imshow('Detected Faces', image)
cv2.waitKey(0)
cv2.destroyAllWindows()