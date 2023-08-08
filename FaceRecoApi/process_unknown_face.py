# mail unknown faces once to a specified email

# this separate program is written separately
# avoid circular import issues

import os
import time
import numpy as np
import json
import cv2 as cv
from faces import get_json_path, add_face

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Example usage
sender_email = "facereco3@gmail.com"
sender_password = "elvcnipsgokhjvuo"
receiver_email = "shyamendrahazra@gmail.com"
subject = "Sending unknown faces via email"
message = "Unknown faces found in webcam."
def mail_unknown_faces(frame):
    print("Inside mail unknown")
    current_directory = os.path.dirname(os.path.abspath('__file__'))
    output_filename = os.path.join(current_directory, 'assets'
                                   ,'Unknown_Faces', 'image_')
    output_filename = output_filename + str(time.time()) + ".jpg"

    if len(frame) > 0:
        _, image_data = cv.imencode('.jpg', frame)
        with open(output_filename, "wb") as image_file:
            image_file.write(image_data)

        with open(output_filename, "rb") as image_file:
            image = image_file.read()

        # Create a multipart message
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject

        # Add the message body
        msg.attach(MIMEText(message, "plain"))

        # Load and attach the image
        img = MIMEImage(image)
        img.add_header("Content-Disposition", "attachment", filename="unknown.jpg")
        msg.attach(img)

        # Establish an SMTP connection
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            print("Logging in : (" + sender_email + ")...")
            server.login(sender_email, sender_password)
            print("Logged in to server.")
            print("Sending mail to: " + receiver_email + "...")
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print("Mail sent successfully.")


def process_unknown_faces(frame, unmatched_faces, unmatched_encodings):
    """
    :param frame: the image from where unknown faces will be found
    :param unmatched_faces: the dlib rectangle coordinates of 
        unmatched/unknown faces
    :param unmatched_encodings: enconding of the unmatched/unknown faces
    """
    # check if the unknown face is already known
    path = get_json_path('u')
    with open(path, "r") as json_read:
        unknown_face_data = json.load(json_read)
    for face in unmatched_encodings:
        for face_data in unknown_face_data:
            for _, encoding in face_data.items():
                compare_distance = np.linalg.norm(encoding - face, axis=0)
                if compare_distance <= 0.6:
                    return

        # add the unknown faces in the unknown_faces.json file
        face = face.tolist()
        add_face(face, 'u')

        # mail the unknown faces
        for face in unmatched_faces:
            cv.rectangle(frame, 
                        (face.left(), face.top()), 
                        (face.right(), face.bottom()), 
                        (0, 255, 0), 2)
            # print(type(frame))
            mail_unknown_faces(frame)
