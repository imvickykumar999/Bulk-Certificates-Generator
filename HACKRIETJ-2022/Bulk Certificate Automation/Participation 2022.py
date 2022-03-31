# https://docs.google.com/spreadsheets/d/15s9lojXefKIbXUOp0U0Tmg5aFsiSR4G37pHR9bLQgXU/edit?resourcekey#gid=220112151
# Custom Code 2021 : https://github.com/imvickykumar999/Bulk-Certificates-Generator
# Custom Code 2022 : https://github.com/imvickykumar999/HACKRIETJ-2022

# ...first run dance.py to save excel file.

from PIL import Image, ImageDraw, ImageFont
import pandas as pd, os

df = pd.read_excel('HACKRIETJ-2022 (Responses).xlsx')
teamleader = list(df['FULL NAME ( Team Leader )'])

member1 = list(df['Full Name ( Member 2 )'])
member2 = list(df['Full Name ( Member 3 )'])
member3 = list(df['Full Name ( Member 4 )'])
mentor = list(df['Name of MENTOR'])

namelist = [teamleader, member1, member2, member3, mentor]
collegelist = list(df['College Name ( All team members must belong to same College )'])
font = ImageFont.truetype('Allura-Regular.ttf', 45)

try:
    os.mkdir('Certificate')
    os.mkdir('Certificate/Mentor')
    os.mkdir('Certificate/Student')
    os.mkdir('Certificate/Winners')
except:
    pass

def generator(text, font, loc, name):
    img = Image.open('template.png')
    draw = ImageDraw.Draw(img)

    draw.text(
            xy=(358,335), # hit and trial value.
            text='{}'.format(text),
            fill=(0,0,0),
            align='center',
            font=font,
             )

    img.save(f'{loc}/{name}.png')


def create(listed, desig):
    try:
        for j in range(len(listed)):
            for i in range(len(df)):

                name = listed[j][i]
                college = collegelist[i]

                text = f'''
                This Certificate Awarded  To
                {name}

                {desig} of
                {college}

                For  their  Participation  in HACKRIETJ-22
                Held  on  30 March 2022

                by Rajasthan Institute of Engineering and  Technology, Jaipur.
                '''

                generator(text, font, f'Certificate/{desig}', name)
    except Exception as e:
        pass


# print('Students... ', namelist[:-1])
create(namelist[:-1], 'Student')

# print('Mentor... ', [namelist[-1]])
create([namelist[-1]], 'Mentor')


wind = {
        0 : (['Preethika N C', 'Subiksha T', 'Swetha Sridevi N'], 'Bannari Amman Institute Of Technology', '1st'),
        1 : (['Narottam Tomar', 'Akshay Pareek', 'Prabhat Singh', 'Vicky Kumar'], 'Rajasthan Institute Of Engineering And Technology', '2nd'),
        2 : (['Mahipal Pareek', 'Uma kanwar'], 'Vidya Jyothi institute of Technology', '3rd')
       }

for i in range(len(wind)):
    for j in range(len(wind[i][0])):

        winners = f'''
                This Certificate Awarded  To
                {wind[i][0][j]}

                student of
                {wind[i][1]}

                Secured  {wind[i][2]}  Rank  in  HACKRIETJ-22
                Held  on  30 March 2022

                by Rajasthan Institute of Engineering and  Technology, Jaipur.
        '''

        generator(winners, font, 'Certificate/Winners', wind[i][0][j])
