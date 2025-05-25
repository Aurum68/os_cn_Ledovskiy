import imaplib
import email
import os
from email.header import decode_header
import logging

# Настройки логирования
logging.basicConfig(filename='email_receiver.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def fetch_emails():
    username = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')

    # Подключение к почтовому ящику
    mail = imaplib.IMAP4_SSL('imap.yandex.com')
    try:
        mail.login(username, password)
    except Exception as e:
        logging.error("Failed to send email: %s", e)

    # Выбор почтового ящика
    mail.select("inbox")

    # Поиск всех писем
    status, messages = mail.search(None, 'ALL')
    email_ids = messages[0].split()

    # Получение списка писем
    logging.info(f"Total emails: {len(email_ids)}")

    if not email_ids:
        logging.info("No emails found.")
        return

    print_emails(mail, email_ids, [i for i in range(len(email_ids))])
    print()
    print()
    print("Last email")
    print_emails(mail, email_ids, [-1])


    # Закрытие соединения
    mail.logout()


def print_emails(mail: imaplib.IMAP4_SSL, email_ids: list, indexes: list[int]) -> None:
    email_ids_current = [email_ids[i] for i in indexes]
    for email_id in email_ids_current:
        # Получение письма
        status, msg_data = mail.fetch(email_id, '(RFC822)')
        msg = email.message_from_bytes(msg_data[0][1])

        # Декодирование заголовка
        subject, encoding = decode_header(msg['Subject'])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding if encoding else 'utf-8')

        # Получение отправителя
        from_ = msg.get('From')
        body = ""

        # Получение текста письма
        if msg.is_multipart():
            # Если письмо многосоставное
            for part in msg.walk():
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))

                # Извлечение текстовой части
                if content_type == "text/plain" and "attachment" not in content_disposition:
                    body = part.get_payload(decode=True).decode()  # Декодируем тело письма
                    break
        else:
            # Если письмо не многосоставное
            body = msg.get_payload(decode=True).decode()  # Декодируем тело письма

        # Печать заголовков и текста письма
        print(f"Subject: {subject}")
        print(f"From: {from_}")
        print(f"Body:\n{body}\n")
        logging.info(f"Processed email: {subject} from {from_}")


if __name__ == "__main__":
    fetch_emails()