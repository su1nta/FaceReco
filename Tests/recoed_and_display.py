import cv2
from datetime import datetime

# Set video parameters
frame_width = 640
frame_height = 480
fps = 15.0

# Get current date and time
current_datetime = datetime.now().strftime("%Y%m%d-%H%M%S")

# Specify custom directory for output
output_directory = "output/"

# Generate output filename with custom directory
output_file = f"{output_directory}/output_{current_datetime}.mp4"

# Capture frames from input source (e.g., webcam)
cap = cv2.VideoCapture(0)



# Create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))

while True:
    # Read frame from the video capture
    ret, frame = cap.read()

    if not ret:
        break

    # Flip the frame horizontally
    flipped_frame = cv2.flip(frame, 1)

    # Write the flipped frame to the video file
    # out.write(flipped_frame)

    # Display the flipped frame (optional)
    cv2.imshow('Flipped Frame', flipped_frame)

    # Stop recording if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
# out.release()
cap.release()
cv2.destroyAllWindows()
