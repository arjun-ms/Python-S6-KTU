from PIL import Image,ImageEnhance

img = Image.open('input.jpeg')
enh = ImageEnhance.Brightness(img)
# brightens
# op = enh.enhance(2.5)
# no change
# op = enh.enhance(1)
# darkens
op = enh.enhance(0.5)

op.save("output.png")