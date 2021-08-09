# https://drive.google.com/drive/folders/1VVF-K5QqWQcvtnBZYpQAT6jgb7HOmgCf?usp=sharing

# Custom Code : https://github.com/imvickykumar999/Bulk-Certificates-Generator

from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

df = pd.read_excel('Shortlisted Teams.xlsx')
teamleader = list(df['FULL NAME ( Team Leader )'])

member1 = list(df['Full Name ( Member 1 )'])
member2 = list(df['Full Name ( Member 2 )'])
member3 = list(df['Full Name ( Member 3 )'])

namelist = [teamleader, member1, member2, member3]
collegelist = list(df['College Name ( All team members must belong from same College )'])
font = ImageFont.truetype('arial.ttf',40)

def generator(text, font, loc, name):

    img = Image.open('Certificate.png')
    draw = ImageDraw.Draw(img)

    draw.text(
            xy=(375,530),
            text='{}'.format(text),
            fill=(0,0,0),
            align='center',
            font=font,
             )

    img.save(f'{loc}/{name}.png')


for j in range(len(namelist)):
    for i in range(len(df)):

        name = namelist[j][i]
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

        generator(text, font, 'participants pictures', name)

wind = {
        0 : ('Karna', ['Vignesh M', 'Praveen S'], 'Government College of Technology,Coimbatore', '1st'),
        1 : ('The Grandsons', ['Nishant Giri', 'Faizan Alam'], 'Kalinga Institute of Industrial Technology, Bhubaneswar', '2nd'),
        2 : ('Cocokasaya', ['D.v.n.kameswari', 'M.divya', 'K.vasanth'], 'Vidya Jyothi institute of technology', '3rd')
       }

for i in range(len(wind)):
    for j in range(len(wind[i][1])):
        winners = f'''

        This is to certify that
        "{wind[i][1][j]}"

        student of
        "{wind[i][2]}"

        secured {wind[i][3]} Rank in HACKRIETJ-2021
        which held on 26/6/2021 by
        "Rajasthan Institute of Engineering and Technology, Jaipur".
        '''

        # print(wind[i][1][j])
        generator(winners, font, 'winners pictures', wind[i][1][j])
