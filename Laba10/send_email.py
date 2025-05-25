import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import logging

# Настройки логирования
logging.basicConfig(filename='email_sender.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def send_email(subject, body, to_email, attachment_path):
    from_email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Добавление текста письма
    msg.attach(MIMEText(body, 'plain'))

    # Добавление вложения
    if attachment_path:
        with open(attachment_path, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={attachment_path}')
            msg.attach(part)

    # Отправка письма
    try:
        with smtplib.SMTP('smtp.yandex.com', 587) as server:
            server.starttls()
            server.login(from_email, password)
            server.send_message(msg)
            logging.info("Email sent successfully.")
    except Exception as e:
        logging.error("Failed to send email: %s", e)

if __name__ == "__main__":
    send_email("Test Subject", "This is the body", "lanton@stud.kantiana.ru", "file.txt")