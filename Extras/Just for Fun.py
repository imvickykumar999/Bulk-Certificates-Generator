# https://drive.google.com/drive/folders/1VVF-K5QqWQcvtnBZYpQAT6jgb7HOmgCf?usp=sharing

# Custom Code : https://github.com/imvickykumar999/Bulk-Certificates-Generator

from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

font = ImageFont.truetype('arial.ttf', 40)
winners = f'''

This is to certify that
"Mr. Ankit Malpani"

student of
"Rajasthan Institute of Engineering and Technology, Jaipur"

secured 1st Rank in HACKRIETJ-2021
which held on 26/6/2021 by
"Rajasthan Institute of Engineering and Technology, Jaipur".
'''

img = Image.open('Certificate.png')
draw = ImageDraw.Draw(img)

draw.text(
        xy=(475,530),
        text='{}'.format(winners),
        fill=(0,0,0),
        align='center',
        font=font,
         )

img.save('Just for Fun.png')
