import manual_edge

import manual_gauss
import matplotlib.pyplot as plt

# carrega a imagem em uma variável
imagemOriginal = plt.imread('C:/Users/flavi/Pictures/principal.jpg')  # caminho para a imagem na máquina
# aplica o filtro de sobel
imagemFinal = manual_edge.sobel_manual(imagemOriginal)
# aplica o filtro de gauss
# imagemFinal = manual_gauss.gauss_manual(imagemOriginal)

# compara antes e depois
fig, axes = plt.subplots(ncols=2, figsize=(10, 5))
axes[0].set_title("Antes")
axes[0].imshow(plt.imread('C:/Users/flavi/Pictures/principal.jpg'))
axes[1].set_title("Depois")
axes[1].imshow(imagemFinal)
plt.show()
