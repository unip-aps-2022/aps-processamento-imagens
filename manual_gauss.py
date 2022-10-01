from PIL import Image
import matplotlib.pyplot as plt
import cv2 as cv2
import nupy as np

filtroHorizontalGauss = [[1, 2, 1], [2, 4, 2], [1, 2, 1]]
filtroVerticalGauss = [[1, 2, 1], [2, 4, 2], [1, 2, 1]]

imagem = plt.imread('C:/Users/flavi/Pictures/t3.jpg')

n, m, d = imagem.shape
gaussImagem = imagem.copy()

for linha in range(3, n - 2):
    for coluna in range(3, m - 2):
        tempR = 0
        tempG = 0
        tempB = 0
        count = 0
        areaPixels = imagem[linha - 1:linha + 2, coluna - 1:coluna + 2, 0]

        # for matrizH in range(linha - 1, linha + 2):
        #     for matrizV in range(coluna - 1, coluna + 2):
        #         R, G, B = imagem[matrizH, matrizV]
        #         tempR += R
        #         tempG += G
        #         tempB += B
        #         count += 1
        #
        # valorR = tempR/count
        # valorG = tempG/count
        # valorB = tempB/count
        # gaussImagem[linha, coluna] = (valorR, valorG, valorB)

# fig, axes = plt.subplots(ncols=2, figsize=(10, 5))
# axes[0].imshow(imagem)
# axes[0].set_title("image pedalada")
# axes[1].imshow(gaussImagem)
# axes[1].set_title("image mudada")
# plt.show()

img = cv2.imwrite("C:/Users/flavi/Pictures/gauss.jpg", gaussImagem)
