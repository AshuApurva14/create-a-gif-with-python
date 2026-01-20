import imageio.v3 as iio
from PIL import Image
import numpy as np

file_names = ['/workspaces/create-a-gif-with-python/images/IMG_20251224_102014.jpg', '/workspaces/create-a-gif-with-python/images/IMG_20251224_102700.jpg', '/workspaces/create-a-gif-with-python/images/IMG_20251224_105826.jpg', '/workspaces/create-a-gif-with-python/images/IMG_20251224_105831.jpg', '/workspaces/create-a-gif-with-python/images/IMG_20251224_110735.jpg']

images = []

# Load first image to get a reference size
first_img = iio.imread(file_names[0])
target_size = (first_img.shape[1], first_img.shape[0]) # (width, height)


for filename in file_names: 
    img = Image.open(filename).convert('RGB') # Ensure consistent color mode
    img_resized = img.resize(target_size, Image.Resampling.LANCZOS)

    images.append(np.array(img_resized))

iio.imwrite('my.gif', images, duration = 500, loop = 0)


