import cv2
import matplotlib.pyplot as plt


#Questão 2:
caminho_imagem = 'img\homemaranha.jpg'
imagem = cv2.imread(caminho_imagem)

cor_original = cv2.cvtColor(imagem,cv2.COLORMAP_RAINBOW)
cor_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

plt.subplot(121),plt.imshow(cor_original, cmap= 'gray')
plt.title('Imagem original'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(cor_cinza,cmap = 'gray')
plt.title('Imagem editada'), plt.xticks([]), plt.yticks([])
plt.show()