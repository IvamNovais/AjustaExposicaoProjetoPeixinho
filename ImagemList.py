#Biblioteca
import PIL
# Classe para fazer a manipulação de imagens:
from PIL import Image

# Carregar um imagem a partir do disco:
image = Image.open("imagens/frame9.jpg")

# Visualizando a imagem:
image

# Formato da imagem:
print(image.format)

JPEG

# Canal do formato de pixels:
print(image.mode)

RGB

# Dimensões da imagem em pixels:
print(image.size)

(639, 358)

Image.open("imagens/pixel-rgb.png")

# Importando as bibliotecas para visualização das imagens:
from matplotlib import image
from matplotlib import pyplot
# Carregando imagem como um array NumPy:
data = image.imread("imagens/frame9.jpg")
# Imprimindo o conteúdo do array NumPy:
print(data)

[[[148 188 188]
  [148 188 188]
  [148 188 188]
  ...
  [119 145 146]
  [119 145 146]
  [119 145 144]]

 [[149 189 189]
  [149 189 189]
  [149 189 189]
  ...
  [119 145 146]
  [119 145 146]
  [118 144 145]]

 [[150 190 190]
  [150 190 190]
  [150 190 190]
  ...
  [118 144 145]
  [118 144 145]
  [118 144 145]]

 ...

 [[132 137 105]
  [128 135 102]
  [124 131  98]
  ...
  [ 16  22  44]
  [ 15  27  49]
  [ 22  39  59]]

 [[129 134 102]
  [127 134 101]
  [123 130  99]
  ...
  [ 66  64  85]
  [ 51  53  76]
  [ 38  46  67]]

 [[124 129  97]
  [124 131  98]
  [125 132 101]
  ...
  [ 39  30  49]
  [ 46  41  64]
  [ 52  52  76]]]

  # Imprimindo as propriedades do array de pixels:

print(data.dtype)
uint8

print(data.shape)
(358, 639, 3)

print(data.max())
255

print(data.min())
0
# Exibindo o array de pixels como uma imagem:
pyplot.imshow(data)
