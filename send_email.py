import smtplib
import ssl
import os


def send_email(message):
    host = 'smtp.gmail.com'
    port = 465

    username = 'tokarski.pythonportfolio@gmail.com'
    password = os.getenv('PASSWORD')

    receiver = 'tomasz.tokarski93@gmail.com'
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host=host, port=port, context=context, timeout=120) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)