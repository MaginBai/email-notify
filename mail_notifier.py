import smtplib
from email.mime.text import MIMEText
from config import *


class MailNotifier:
    def __init__(self):
        self.smtp_server = SMTP_SERVER
        self.smtp_port = SMTP_PORT
        self.email = EMAIL
        self.__password = PASSWORD

    def send_email(self, to_email, subject, message_body):
        msg = MIMEText(message_body, 'plain', 'utf-8')
        msg['Subject'] = subject
        msg['From'] = self.email
        msg['To'] = to_email

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.email, self.__password)
                server.sendmail(self.email, to_email, msg.as_string())
                print(f"The notification was sent successfully {to_email}")
        except smtplib.SMTPException as e:
            print(f"Sending error: {e}")
