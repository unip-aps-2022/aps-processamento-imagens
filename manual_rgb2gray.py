from PIL import Image
import matplotlib.pyplot as plt

# image = Image.open(r"C:/Users/flavi/Pictures/t.jpg")
# image = image.convert('RGB')
from numpy import array


def rgb2gray(imageBefore):
    # x = imageBefore.getdata()
    # a, b = x.size
    a, b, c = imageBefore.shape
    # x = imageBefore.load()
    # imageGrayscale = Image.new(mode="RGB", size=(a, b), color=(0, 0, 0))
    imageGrayscale = imageBefore.copy()

    # y = imageGrayscale.load()

    for i in range(a):
        for j in range(b):
            R, G, B = imageBefore[i, j]
            avg = (int(R) + int(G) +int(B)) / 3
            imageGrayscale[i, j] = (avg, avg, avg)

    return imageGrayscale

# fig, axes = plt.subplots(ncols=2, figsize=(10, 5))
# axes[0].imshow(image)
# axes[0].set_title("image pedalada")
# axes[1].imshow(image_grayscale)
# axes[1].set_title("image grayscale")
# plt.show()
