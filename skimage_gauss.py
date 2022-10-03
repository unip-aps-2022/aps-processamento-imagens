import numpy as np
import matplotlib.pyplot as plt

from skimage import filters
from skimage.data import camera
from skimage.util import compare_images

image = camera()
edge_sobel = filters.gaussian(image)

fig, axes = plt.subplots(ncols=2, sharex=True, sharey=True, figsize=(8, 4))

axes[0].set_title("image pedalada")
axes[0].imshow(image)
axes[1].set_title("image com filtro")
axes[1].imshow(edge_sobel)
plt.show()
