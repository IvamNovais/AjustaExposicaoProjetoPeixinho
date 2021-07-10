#Biblioteca

import PIL
import cv2
import numpy as np
from PIL import Image

# Carregar um imagem a partir do disco:
image = Image.open("frame10.jpg")

# Formato da imagem:
print(image.format)

#JPEG

# Canal do formato de pixels:
print(image.mode)

#RGB

# Dimensões da imagem em pixels:
print(image.size)

Image.open("frame10.jpg")

# Importando as bibliotecas para visualização das imagens:
from matplotlib import image
from matplotlib import pyplot
# Carregando imagem como um array NumPy:
data = image.imread("frame10.jpg")
# Imprimindo o conteúdo do array NumPy:
print(data)

# Exibindo o array de pixels como uma imagem:
pyplot.imshow(data)
