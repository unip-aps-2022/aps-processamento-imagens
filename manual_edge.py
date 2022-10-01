import matplotlib.pyplot as plt

# filtro vertical e horizontal
filtroVerticalSobel = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
filtroHorizontalSobel = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
# lê a foto "t"
imagem = plt.imread('C:/Users/flavi/Pictures/t4.jpg')

# armazena o x, y e z da foto e inicia foto final
n, m, d = imagem.shape
bordasImagem = imagem.copy()

# itera por todos os pixels
for linha in range(3, n - 2):
    for coluna in range(3, m - 2):
        # cria area da imagem de tamanho 3 por 3
        areaPixels = imagem[linha - 1:linha + 2, coluna - 1:coluna + 2, 0]

        # aplica o filtro de sobel na vertical
        sobelVerticalFiltroAplicado = filtroVerticalSobel * areaPixels
        somaVertical = sobelVerticalFiltroAplicado.sum() / 4

        # aplica o filtro de sobel na horizontal
        sobelHorizontalFiltroAplicado = filtroHorizontalSobel * areaPixels
        somaHorizontal = sobelHorizontalFiltroAplicado.sum() / 4

        # faz a soma ponderada do filtro vertical e horizontal elevados a 2
        calculoBordas = (somaVertical ** 2 + somaHorizontal ** 2) ** .5

        # insere a soma ponderada na imagem
        bordasImagem[linha, coluna] = [calculoBordas] * 3

# previne erro de sair das bordas
bordasImagem = bordasImagem / bordasImagem.max()

# mostra
fig, axes = plt.subplots(ncols=1, figsize=(10, 5))
axes.set_title("Num sei")
axes.imshow(bordasImagem)
plt.show()
