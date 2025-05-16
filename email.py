import smtplib
from email.message import EmailMessage

def send_email(to, subject, body):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = 'your_email@example.com'
    msg['To'] = to
    msg.set_content(body)

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login('your_email@example.com', 'your_password')
        smtp.send_message(msg)