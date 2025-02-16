import os

from mailersend import emails

TOKEN = os.environ["TOKEN"]
EMAIL_TEMPLATE_PATH = os.path.join("static", "email_template.html")
EMAIL_SUBJECT = os.environ["EMAIL_SUBJECT"]
SENDER_EMAIL = os.environ["SENDER_EMAIL"]
RECIPIENTS = os.environ["RECIPIENTS"]

mailer = emails.NewEmail(TOKEN)


def get_email_content():
    with open(EMAIL_TEMPLATE_PATH, 'r', encoding='utf-8') as email_template:
        html_content = email_template.read()
        return html_content


mail_body = {}

mail_from = {
    "name": "Najam Stana",
    "email": SENDER_EMAIL,
}

recipients = [
    {
        "name": "Jurica Migač",
        "email": RECIPIENTS,
    }
]
email_body = get_email_content()
mailer.set_mail_from(mail_from, mail_body)
mailer.set_mail_to(recipients, mail_body)
mailer.set_subject(EMAIL_SUBJECT, mail_body)
mailer.set_html_content(email_body, mail_body)

if __name__ == "__main__":
    try:
        response = mailer.send(mail_body)
    except Exception as e:
        print(f"An error occurred: {e}")
