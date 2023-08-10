
from PIL import Image, ImageDraw, ImageFont
import time
order = ("15896", "15845")
img = Image.open("blank.png")

draw = ImageDraw.Draw(img)
font = ImageFont.truetype("arial.ttf", 24)
draw.text((0,0), order[0], (0,0,0), font=font)
c = (0,0)
for i in range(1, len(order)):
 
    a = c[1] +24
    print(a)
    print(order[i])
    draw.text((0,a), order[i], (0,0,0), font=font)

img.save("test.png")