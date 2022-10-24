def rgb2gray(imageBefore):
    a, b, c = imageBefore.shape
    imageGrayscale = imageBefore.copy()

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
