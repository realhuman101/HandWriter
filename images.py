from PIL import Image
import os
import sys
from random import choice
txt = open("dummy.txt", "r")
BG=Image.open("fonts/fontSetup/bg.png") 
#BG = BG.resize((1500,500))
sheet_width=BG.width
gap, ht = 0, 0
paths = ["font1", "font2"]
specials = ["specialChars1"]
digits = ["digits1", "digits2"]
fullStops = ["stop1", "stop2", "stop3"]

for i in txt.read().replace("\n",""):
    selected = [choice(paths), choice(digits), choice(specials), choice(fullStops)]

    if (33 <= ord(i) <= 47 or 58 <= ord(i) <= 64 or 91 <= ord(i) <= 96 or 123 <= ord(i) <= 126) and ord(i) != 46:
        try:
            cases = Image.open("fonts/{fontPath}/{}.png".format(str(ord(i)), fontPath = selected[2]))
        except Exception:
            try:
                cases = Image.open("fonts/{fontPath}/{}.jpeg".format(str(ord(i)), fontPath = selected[2]))
            except Exception:
                print(f"{i} was not found in path fonts/{selected[2]}")
    elif 48 <= ord(i) <= 57:
        try:
            cases = Image.open("fonts/{fontPath}/{}.png".format(str(ord(i)), fontPath = selected[1]))
        except Exception:
            try:
                cases = Image.open("fonts/{fontPath}/{}.jpeg".format(str(ord(i)), fontPath = selected[1]))
            except Exception:
                print(f"{i} was not found in path fonts/{selected[1]}")
    elif ord(i) != 32 and (65 <= ord(i) <= 90 or 97 <= ord(i) <= 122):
        try:
            cases = Image.open("fonts/{fontPath}/{}.png".format(str(ord(i)), fontPath = selected[0]))
        except Exception:
            try:
                cases = Image.open("fonts/{fontPath}/{}.jpeg".format(str(ord(i)), fontPath = selected[0]))
            except Exception:
                print(f"{i} was not found in path fonts/{selected[0]}")
    elif ord(i) == 32:
        cases = Image.open("fonts/fontSetup/32.png")
    elif ord(i) == 46:
        try:
            cases = Image.open("fonts/fontSetup/{}.png".format(selected[3]))
        except Exception:
            try:
                cases = Image.open("fonts/fontSetup/{}.jpeg".format(selected[3]))
            except Exception:
                print(f"{i} was not found as {selected[3]}")
    else:
        continue
    BG.paste(cases, (gap, ht))
    size = cases.width
    height=cases.height
    #print(size)
    gap+=size
    if sheet_width < gap or len(i)*115 >(sheet_width-gap):
        gap,ht=0,ht+140
print(gap)
print(sheet_width)
BG.show()

txt.close()
while True:
    input("Press enter to run again... ")
    os.execl(sys.executable, sys.executable, *sys.argv)