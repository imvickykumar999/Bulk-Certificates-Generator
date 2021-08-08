# https://drive.google.com/drive/folders/1VVF-K5QqWQcvtnBZYpQAT6jgb7HOmgCf?usp=sharing

from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

df = pd.read_excel('Shortlisted Teams.xlsx')
namelist = list(df['FULL NAME ( Team Leader )'])
collegelist = list(df['College Name ( All team members must belong from same College )'])
font = ImageFont.truetype('arial.ttf',40)

for i in range(len(df)):
    img = Image.open('Certificate.png')
    draw = ImageDraw.Draw(img)

    name = namelist[i]
    college = collegelist[i]
    text = f'''

    This is to certify that
    "{name}"

    student of
    "{college}"

    has participated in HACKRIETJ-2021
    which held on 26/6/2021 by
    "Rajasthan Institute of Engineering and Technology, Jaipur".
    '''

    draw.text(xy=(470,530),
            text='{}'.format(text),
            fill=(0,0,0),
            align='center',
            font=font)

    img.save('pictures/{}.png'.format(f'{name}'))


# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# from email import encoders
#
# fromaddr = "imvickykumar999@gmail.com"
# toaddr = list(df['EMAIL ID ( Team Leader )'])[0]
#
# # instance of MIMEMultipart
# msg = MIMEMultipart()
#
# # storing the senders email address
# msg['From'] = fromaddr
#
# # storing the receivers email address
# msg['To'] = toaddr
#
# # storing the subject
# msg['Subject'] = "Subject of the Mail"
#
# # string to store the body of the mail
# body = "Body_of_the_mail"
#
# # attach the body with the msg instance
# msg.attach(MIMEText(body, 'plain'))
#
# # open the file to be sent
# filename = "File_name_with_extension"
# attachment = open("Path of the file", "rb")
#
# # instance of MIMEBase and named as p
# p = MIMEBase('application', 'octet-stream')
#
# # To change the payload into encoded form
# p.set_payload((attachment).read())
#
# # encode into base64
# encoders.encode_base64(p)
#
# p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
#
# # attach the instance 'p' to instance 'msg'
# msg.attach(p)
#
# # creates SMTP session
# s = smtplib.SMTP('smtp.gmail.com', 587)
#
# # start TLS for security
# s.starttls()
#
# # Authentication
# s.login(fromaddr, "Password_of_the_sender")
#
# # Converts the Multipart msg into a string
# text = msg.as_string()
#
# # sending the mail
# s.sendmail(fromaddr, toaddr, text)
#
# # terminating the session
# s.quit()
