from PIL import Image
import matplotlib.pyplot as plt

image = Image.open(r"C:/Users/flavi/Pictures/t.jpg")
image = image.convert('RGB')

x = image.getdata()
a, b = x.size
x = image.load()
image_grayscale = Image.new(mode="RGB",
                            size=(a, b),
                            color=(0, 0, 0))

y = image_grayscale.load()

for i in range(a):
    for j in range(b):
        R, G, B = x[i, j]
        avg = (R+G+B)/3
        y[i, j] = (int(avg), int(avg), int(avg))

fig, axes = plt.subplots(ncols=2, figsize=(10, 5))
axes[0].imshow(image)
axes[0].set_title("image pedalada")
axes[1].imshow(image_grayscale)
axes[1].set_title("image grayscale")
plt.show()


