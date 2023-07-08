import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


def send_email(sender_email, sender_password, receiver_email, subject, message, image_path):
    # Create a multipart message
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    # Add the message body
    msg.attach(MIMEText(message, "plain"))

    # Load and attach the image
    with open(image_path, "rb") as fp:
        img = MIMEImage(fp.read())
    img.add_header("Content-Disposition", "attachment", filename="img.jpg")
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


# Example usage
sender_email = "example@gmail.com"
sender_password = "password"
receiver_email = "example2@gmail.com"
subject = "Sending an image via email"
message = "Hello, I'm sending you an image."
image_path = "compare2.jpg"

send_email(sender_email, sender_password, receiver_email, subject, message, image_path)
