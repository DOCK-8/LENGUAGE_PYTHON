import sys
from PIL import Image, ImageDraw

with Image.open("test.jpg") as im:
    lenght = 100 #border size
    size = im.size
    new_size = (size[0]+100,size[1]+100)
    image = Image.new("RGB", new_size, '#0099ff')
    box = tuple((n - o) // 2 for n, o in zip(new_size, size))
    image.paste(im, box)
    image.save('new.jpg')
