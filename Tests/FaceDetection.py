import dlib
import cv2

# Load the image
path = input("Enter the path of the image: ")
image = cv2.imread(path)

# resize the image
small_image = cv2.resize(image, (0, 0), fx=0.50, fy=0.50)

# Initialize the face detector
detector = dlib.get_frontal_face_detector()

# Detect all faces in the image
face_rects = detector(small_image, 0)

# Draw each rectangle on the image
for rect in face_rects:
    cv2.rectangle(small_image, (rect.left(),rect.top()), (rect.right(),rect.bottom()), (255, 0, 0), 2)

# Display the image with detected faces
cv2.imshow('Detected Faces', small_image)

# display the object types

print("small_image: ", type(small_image))
print("detector: ", type(detector))
print("face_rects: ", type(face_rects))

cv2.waitKey(0)
cv2.destroyAllWindows()