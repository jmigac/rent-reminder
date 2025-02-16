import os

from mailersend import emails

TOKEN = os.environ["TOKEN"]
EMAIL_TEMPLATE_PATH = os.path.join("static", "email_template.html")
SENDER_EMAIL = os.environ["SENDER_EMAIL"]
RECIPIENT_NAME = os.environ["RECIPIENT_NAME"]
RECIPIENT_EMAIL = os.environ["RECIPIENT_EMAIL"]
CC_NAME = os.environ["CC_NAME"]
CC_EMAIL = os.environ["CC_EMAIL"]

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
        "name": RECIPIENT_NAME,
        "email": RECIPIENT_EMAIL,
    }
]

cc = [
    {
        "name": CC_NAME,
        "email": CC_EMAIL
    }
]
email_body = get_email_content()
mailer.set_mail_from(mail_from=mail_from, message=mail_body)
mailer.set_mail_to(mail_to=recipients, message=mail_body)
mailer.set_cc_recipients(cc_recipient=cc, message=mail_body)
mailer.set_html_content(content=email_body, message=mail_body)

if __name__ == "__main__":
    try:
        response = mailer.send(mail_body)
    except Exception as e:
        print(f"An error occurred: {e}")
