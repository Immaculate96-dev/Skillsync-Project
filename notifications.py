import click
import smtplib
from email.message import EmailMessage

# Yet to modify this code
# This function will notify users of appointments and add events to their calendar
def send_email_notification(to_email, subject, body):
    sender_email = "your-email@gmail.com"
    sender_password = "your-app-password"

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to_email
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
        click.echo(f"Email sent successfully to {to_email}")
    except Exception as e:
        clic.echok(f"Error sending email: {e}")


send_email_notification("mentee@example.com", "Upcoming Session", "You have a session scheduled at 10 AM.")
