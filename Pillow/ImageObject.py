# import image module
from PIL import Image

# # import an image
# img = Image.open('panda.jpg')
# # show that image
# img.show('Panda')

# alternative way to import an image
with Image.open('panda.jpg') as pandaimg:
    print(type(pandaimg))
    # pandaimg.show()

# create an image object
# Image.new(format, dimension)  where format is 'RGBA', 'CMYK' etc and dimension is (w, h)
# img = Image.new('RGBA', (800, 800))
# img.show()

# saving an image - it can be in a different format
# you gotta uncomment the import an image section
# pandaimg.save('panda.png')


# getting info of an image
# you gotta uncomment the import an image section
# print(pandaimg.size)
# print(pandaimg.format)
# print(pandaimg.format_description)
