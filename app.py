import os
import smtplib
import time
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# SMTP Configuration
SMTP_SERVER = os.environ["SMTP_SERVER"]
SMTP_PORT = os.environ["SMTP_PORT"]
INT_SMTP_PORT = int(SMTP_PORT)
SMTP_USERNAME = os.environ["SMTP_USERNAME"]
SMTP_PASSWORD = os.environ["SMTP_PASSWORD"]
# Email Details
SENDER_EMAIL = os.environ["SENDER_EMAIL"]
RECIPIENTS = os.environ["RECIPIENTS"]
SUBJECT = os.environ["EMAIL_SUBJECT"]
EMAIL_TEMPLATE_PATH = os.path.join("static", "email_template.html")


def get_email_content():
    with open(EMAIL_TEMPLATE_PATH, 'r', encoding='utf-8') as email_template:
        html_content = email_template.read()
        return html_content


def send_email():
    try:
        # Create Email Message
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = RECIPIENTS
        msg["Subject"] = SUBJECT

        # HTML Email Body with <table>
        html_content = get_email_content()
        msg.attach(MIMEText(html_content, "html"))

        # Connect to SMTP Server and Send Email
        server = smtplib.SMTP(SMTP_SERVER, INT_SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECIPIENTS, msg.as_string())
        server.quit()

        print(f"Email sent successfully at {datetime.now()}!")

    except Exception as e:
        print(f"Failed to send email: {e}")


if __name__ == "__main__":
    send_email()
