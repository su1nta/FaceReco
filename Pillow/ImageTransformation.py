# Basic Image transformation will be done here - Rotate, flip, crop, scale
from PIL import Image, ImageColor as ic

img = Image.open('panda.jpg')
print(type(img))
# Rotate an Image
# img.rotate(degree, expand, fillcolor)
# expand is a boolean argument which checks if the image will be expanded or not
# as rotating image can lose image data if the whole image is not expanded
# fillcolor takes an RGB list as input
# img_rotate = img.rotate(45, expand=True, fillcolor=(255, 255, 255))
# img_rotate.show()

# we can use ImageColor module to get RGB value be specifying color as a string
# img_rotate = img.rotate(45, expand=True, fillcolor=ic.getcolor('teal', 'RGB'))
# img_rotate.show()

# get the available colors in ImageColor
# print(ic.colormap)


# Crop an Image
# img.crop((left_x, top_y, right_x, bottom_y))
# img_crop = img.crop((0, 0, 700, 700))
# img_crop.show()


# Flip/Transpose an Image
# img.transpose(Image.option)
# option - FLIP_TOP_BOTTOM; FLIP_LEFT_RIGHT, ROTATE_90, ROTATE_180, ROTATE_270, TRANSPOSE, TRANSVERSE

# img_flip_hor = img.transpose(Image.FLIP_LEFT_RIGHT)
# img_flip_hor.show()
#
# img_transpose = img.transpose(Image.TRANSPOSE)
# img_transpose.show()


# Resize an Image
# img.resize((w, h))
# this method ruins the aspect ratio
# img_resized = img.resize((700, 900))
# img_resized.show()


# Scale an Image
# img.resize((w*scale_factor, h*scale_factor))
scale_factor = 2  # double the size
img_scaled = img.resize((img.size[0]*scale_factor, img.size[1]*scale_factor))
img_scaled.show()
img_scaled.save('panda_big.jpg')
