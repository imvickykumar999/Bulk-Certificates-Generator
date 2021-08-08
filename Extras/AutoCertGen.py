from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

# df = pd.read_excel('Shortlisted Teams.xlsx')
font = ImageFont.truetype('arial.ttf',40)

# for index,j in df.iterrows():
img = Image.open('Certificate.png')
draw = ImageDraw.Draw(img)

name = 'Nikhil Bhardwaj'
college = 'Great Lakes Institute of Management, Gurgaon'
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

img.save('hackrietj2021/{}.png'.format(f'{name}'))
