import smtplib, ssl
import ssl

host = "smtp.gmail.com"
port = 465

username = "dtumaini@gmail.com"
password = "zhzvkdufnhgrmauz"

receiver = "dtumaini@gmail.com"

message = """\
Subject: Hey 
Hi, How you doing? Bye!"""

context = ssl.create_default_context()

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)