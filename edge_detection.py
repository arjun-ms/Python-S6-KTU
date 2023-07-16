from PIL import Image,ImageFilter

img = Image.open('input.jpeg')
gray = img.convert('L')
edge = gray.filter(ImageFilter.FIND_EDGES)
edge.save("output.png")