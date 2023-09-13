import cv2
import matplotlib.pyplot as plt


#Questão 3:
caminho_imagem = 'img\homemaranha.jpg'
imagem = cv2.imread(caminho_imagem)

cor_original = cv2.cvtColor(imagem,cv2.COLORMAP_RAINBOW)
suavizado = cv2.blur(cor_original,(9,9))

plt.subplot(121),plt.imshow(cor_original),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(suavizado),plt.title('Suavizado')
plt.xticks([]), plt.yticks([])
plt.show()

