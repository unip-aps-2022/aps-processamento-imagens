import manual_edge
import matplotlib.pyplot as plt

import manual_gauss

imagemOriginal = plt.imread('C:/Users/flavi/Pictures/principal.jpg')
imagemFinal = manual_edge.sobel_manual(imagemOriginal)
# imagemFinal = manual_gauss.gauss_manual(imagemOriginal)

# tá funcionando mas tem que aumentar o kernel do gauss

fig, axes = plt.subplots(ncols=2, figsize=(10, 5))
axes[0].set_title("Antes")
axes[0].imshow(plt.imread('C:/Users/flavi/Pictures/principal.jpg'))
axes[1].set_title("Depois")
axes[1].imshow(imagemFinal)
plt.show()
