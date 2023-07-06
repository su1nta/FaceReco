# loading window animation with an image loaded
import cv2

# load the image
img_bgr = cv2.imread('example.jpg')
img_resized = cv2.resize(img_bgr, (0, 0), fx=0.25, fy=0.25)
img = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)

# get image width,height
img_width, img_height, _ = img.shape

# loading animation position
loading_position = (10, img_width - 30)

# load the loading frames
loading = []
no_frames = 30
frame_resized = []
for i in range(1, no_frames + 1):
    frame_path = f"loading/frame-{i}.png"
    frame = cv2.imread(frame_path)
    frame_resized = cv2.resize(frame, (0, 0), fx=0.10, fy=0.10)
    loading.append(frame_resized)

# set frame and window stuffs
frame_index = 0
window_name = "Image"
frame_width, frame_height, _ = frame_resized.shape

# set text stuffs
text = "Detecting Faces..."
font = cv2.FONT_HERSHEY_DUPLEX
font_scale = 0.5
font_color = (0, 0, 0)
font_thickness = 1
text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)
_, text_height = text_size
text_position = (frame_height + 20, img_height - 15)

# append the background rectangle
cv2.rectangle(img, (frame_height + 170, img_width - 30), (text_height + 25, img_width - 10), (255, 255, 255), cv2.FILLED)

# display the image with loading animation
while True:
    frame = loading[frame_index]

    combined_image = img.copy()
    combined_image[loading_position[1]:loading_position[1] + frame_height, loading_position[0]:loading_position[0] + frame_width] = frame
    cv2.putText(combined_image, text, text_position, font, font_scale, font_color, font_thickness)
    cv2.imshow(window_name, cv2.cvtColor(combined_image, cv2.COLOR_RGB2BGR))

    key = cv2.waitKey(100)

    if key == ord('q'):
        break

    frame_index = (frame_index + 1) % no_frames

cv2.destroyAllWindows()
