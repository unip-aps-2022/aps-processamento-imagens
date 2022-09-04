from PIL import Image, ImageFilter
import matplotlib.pyplot as plt

image = Image.open(r"C:/Users/flavi/Pictures/t.jpg")
image = image.convert("L")
image = image.filter(ImageFilter.FIND_EDGES)
print("ALO")

fig, axes = plt.subplots(ncols=2, sharex=True, sharey=True, figsize=(8, 4))

axes[0].imshow(image)
plt.show()
