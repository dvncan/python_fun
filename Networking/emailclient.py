import smtplib
from email.mime.text import MIMEText

body = "Hey man this is not a robot email."

msg = MIMEText(body)
msg['From'] = "dundalbrown@gmail.com"
msg['To'] = "duncanb@genuinehealth.com"
msg['Subject'] = "Hello world"

server = smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

server.login("dundalbrown@gmail.com", "good4Nothing@$$", )

server.send_message(msg)

print("Mail Sent")
server.quit()