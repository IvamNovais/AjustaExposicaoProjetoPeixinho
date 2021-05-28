import GetFrame
import cv2

ignorarInicio = 15 #tempo em segundos que sera removido no inicio do video
tirarFim = 15 #tempo em segundos que sera removido no fim do video
# recebe o diretorio do video , o tamanho do corte inicial em segundos e o tanho do corete final em segundos
dir = 'outro'
imagens = GetFrame.GetFrames(dir,ignorarInicio,tirarFim)
cv2.imwrite("img.jpg",imagens[1000])#printa uma imagem para fins de teste
