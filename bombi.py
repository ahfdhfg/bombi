import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

ascii_sms = '''
 ___________________
|  _______________  |
| |               | |
| |  Sender email | |
| |      V1.0     | |
| |               | |
| |_______________| |
|___________________|

'''
print(ascii_sms)
print("This script code was written by Amir")
print("telegram:   https://t.me/CYBER_CYr_a")
print("instagram:MR_TURBO_A ")

sender_email = input("Enter your email: ")
sender_password = input("Enter your password: ")
receiver_email = input("Enter receiver's email: ")

num_messages = int(input("Enter the number of messages to send: "))

for _ in range(num_messages):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Subject of the Email"
    body = input("Enter the message: ")
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)
            print("Email sent successfully!")
    except Exception as e:
        print("An error occurred: ", e)