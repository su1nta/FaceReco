# Loading screen in a opencv window
import cv2

# create a window
window_name = "Loading screen"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

# load the loading animation frames
loading = []
num_frames = 30
for i in range(1, num_frames + 1):      # 30fps
    frame_path = f"loading/frame-{i}.png"
    print(frame_path)
    loading.append(cv2.imread(frame_path))

# display the animation in window
frame_index = 0
while True:
    frame = loading[frame_index]
    text = "Loading images..."

    cv2.putText(frame, text, (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow(window_name, frame)

    key = cv2.waitKey(100)

    if key == ord('q'):
        break

    frame_index = (frame_index + 1) % num_frames

cv2.destroyAllWindows()