import os
import smtplib
import time
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from croniter import croniter

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
CRON_EXPRESSION = os.environ["CRON_EXPRESSION"]
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


def cron_scheduler():
    base_time = datetime.now()
    cron = croniter(CRON_EXPRESSION, base_time)

    while True:
        next_run = cron.get_next(datetime)
        sleep_time = (next_run - datetime.now()).total_seconds()

        if sleep_time > 0:
            print(f"Next email scheduled at {next_run}. Sleeping for {sleep_time:.2f} seconds.")
            time.sleep(sleep_time)
            send_email()


if __name__ == "__main__":
    cron_scheduler()

