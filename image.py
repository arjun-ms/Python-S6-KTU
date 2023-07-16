from PIL import Image,ImageFilter,ImageOps,ImageEnhance

# Open an Image
i1 = Image.open('/home/ams/Pictures/fiverr-gigs/OPEN_AI.png')
# i1.show()

i1.save("image.png")

# rotate an Image
# i2 = i1.rotate(180)
# i2.show()

# Copy an Image
# i3 = i1.copy()
# i3.show()

# Convert to grayscale
# ig=i1.convert('L')
# ig.show()

# Blur the Image
# i4 = i1.filter(ImageFilter.BLUR)
# i4.show()

# Find edges
# ie=i1.filter(ImageFilter.FIND_EDGES)
# ie.show()

# Resize the image
# new=i1.resize((600,300))
# new.show()

# Invert the image 
# iv = ImageOps.invert(i1)
# iv.show()

# Enhance the Image brightness
enh = ImageEnhance.Brightness(i1)
ib = enh.enhance(2.5)
ib.show()