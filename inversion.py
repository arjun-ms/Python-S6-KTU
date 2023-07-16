from PIL import Image,ImageOps

img = Image.open('input.jpeg')
inv = ImageOps.invert(img)
inv.save("output.png")