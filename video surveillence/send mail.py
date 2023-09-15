import cv2
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Function to deduct the fall-down object
def deduct_fall_down_object(frame):
    # Your fall-down object deduction logic here
    # This could involve image processing, object detection, or any other appropriate method

    # Assuming the object is detected and needs to be deducted
    object_name = "Fall-down Object"
    deducted_quantity = 1

    return object_name, deducted_quantity

# Function to send an email report with an attached image
def send_email_report(sender_email, sender_password, receiver_email, subject, body, image_path):
    # Compose the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the body
    msg.attach(MIMEText(body, 'plain'))

    # Attach the image
    with open(image_path, 'rb') as f:
        img_data = f.read()
    image = MIMEImage(img_data, name="Fall-down_Object.jpg")
    msg.attach(image)

    # Connect to the email server and send the email
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email report sent successfully!")
    except Exception as e:
        print("Error sending email:", str(e))

# Main function
def main():
    # Initialize the camera
    cap = cv2.VideoCapture(0)  # Change the index to specify a different camera if needed

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Deduct the fall-down object
        object_name, deducted_quantity = deduct_fall_down_object(frame)

        # Display the deducted object information on the frame
        cv2.putText(frame, f"Deducted: {object_name} x{deducted_quantity}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Show the frame
        cv2.imshow('Camera', frame)

        # Check for the 'q' key to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()

    # Prepare the email report
    sender_email = "deadlyrock765@gmail.com"  # Replace with your email address
    sender_password = "soatrigrvyntbuea"  # Replace with your email password
    receiver_email = "rjprahadeesh30@gmail.com"  # Replace with the recipient's email address
    subject = "Fall-Down Object Deduction Report"
    body = f"The fall-down object '{object_name}' has been deducted. Quantity: {deducted_quantity}."
    image_path = "fall_down_object.jpg"  # Replace with the path to save the captured frame as an image

    # Save the frame as an image
    cv2.imwrite(image_path, frame)

    # Send the email report with the attached image
    send_email_report(sender_email, sender_password,receiver_email, subject, body, image_path)

# Execute the main function
main()
