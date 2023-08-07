import matplotlib.pyplot as plt
from skimage.feature import hog
from skimage import io, color
import os

# Load the image
image_path = '/home/su1nta/Desktop/test3.jpg'
image = io.imread(image_path)
gray_image = color.rgb2gray(image)

# Calculate the HOG features
hog_features, hog_image = hog(gray_image, visualize=True, block_norm='L2-Hys', pixels_per_cell=(16, 16), cells_per_block=(1, 1))
hog_image = hog_image * 4.5

# Create a colormap visualization of the HOG features
plt.figure(figsize=(8, 4))
plt.imshow(hog_image, cmap='gray')
plt.axis('off')

# Save the colormap visualization as a JPEG
output_dir = '/home/su1nta/Desktop/'
output_file = os.path.join(output_dir, 'hog_visualization.jpg')
plt.savefig(output_file, bbox_inches='tight', pad_inches=0, dpi=300)
plt.close()

print(f'HOG visualization saved to {output_file}')
