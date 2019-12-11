import smtplib, ssl, getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 587  # For starttls
smtp_server = "smtp.seznam.cz"
sender_email = "martin@andrasi.cz"
receiver_email = "martin@andrasi.cz"
#receiver_email = "martin.andrasi@parfemgroup.cz"
password = getpass.getpass("Type your password and press enter:")
html = open('./final-html/brasty-personal/index.html')

html_decode = html.read()
content_HTML = MIMEText(html_decode, "html")
#print(html.read().encode('utf-8'))

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, content_HTML.as_string())