import cv2 as cv2
import matplotlib.pyplot as plt
import numpy as np

# imageBeforeGauss = plt.imread('C:/Users/flavi/Pictures/T.jpg')
#
# n, m, d = imageBeforeGauss.shape
# gaussImagem = imageBeforeGauss.copy()


def gauss_manual(imageBeforeGauss):
    gaussImagem = imageBeforeGauss.copy()
    x, y, z = imageBeforeGauss.shape
    for linha in range(3, x - 2):
        for coluna in range(3, y - 2):
            tempR = 0
            tempG = 0
            tempB = 0
            count = 0
            areaPixels = imageBeforeGauss[linha - 1:linha + 2, coluna - 1:coluna + 2, 0]

            # itera por cada pixel, faz a média com os 3 canais de RGB e aplica na imagem nova.
            for matrizH in range(linha - 2, linha + 2):
                for matrizV in range(coluna - 2, coluna + 2):
                    R, G, B = imageBeforeGauss[matrizH, matrizV]
                    tempR += R
                    tempG += G
                    tempB += B
                    count += 1

            valorR = tempR / count
            valorG = tempG / count
            valorB = tempB / count
            gaussImagem[linha, coluna] = (valorR, valorG, valorB)

    # mostra
    # fig, axes = plt.subplots(ncols=2, figsize=(10, 5))
    # axes[0].imshow(imageBeforeGauss)
    # axes[0].set_title("image pedalada")
    # axes[1].imshow(gaussImagem)
    # axes[1].set_title("image mudada")
    # plt.show()

    return gaussImagem
