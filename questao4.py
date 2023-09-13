import cv2


#Questão 4:
caminho_imagem = 'img\homemaranha.jpg'
imagem = cv2.imread(caminho_imagem)

cor_original = cv2.cvtColor(imagem,cv2.COLORMAP_RAINBOW)
cor_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)


#SOBEL
imagem_bordas_sobel_x = cv2.Sobel(cor_cinza, cv2.CV_64F, 1, 0, ksize=3)
imagem_bordas_sobel_y = cv2.Sobel(cor_cinza, cv2.CV_64F, 0, 1, ksize=3)

imagem_bordas_sobel = cv2.magnitude(imagem_bordas_sobel_x, imagem_bordas_sobel_y)
imagem_bordas_sobel = cv2.convertScaleAbs(imagem_bordas_sobel)

cv2.imshow('Detecção de Bordas (Sobel)', imagem_bordas_sobel)
cv2.waitKey(0)
cv2.destroyAllWindows()


#CANNY
bordas_canny = cv2.Canny(cor_cinza, 100, 200)

cv2.imshow('Detecção de Bordas (Canny)', bordas_canny)
cv2.waitKey(0)
cv2.destroyAllWindows()