import sys
from PIL import Image

imagepath = sys.argv[1]

im = Image.open(imagepath)
im = im.rotate(180)
im.save("ans2.png")