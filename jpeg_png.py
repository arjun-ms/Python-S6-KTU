from PIL import Image,ImageFilter

img = Image.open('input.jpeg')

rotated_img = img.rotate(90)

blurr = rotated_img.filter(ImageFilter.BLUR)

blurr.save("output.png")

img.close()