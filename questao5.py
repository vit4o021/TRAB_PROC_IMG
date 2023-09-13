import cv2


#Questão 5:
caminho_imagem = 'img\homemaranha.jpg'
cor_cinza = cv2.imread(caminho_imagem, cv2.IMREAD_GRAYSCALE)
imagem_original = cv2.imread(caminho_imagem)

contornos, _ = cv2.findContours(cor_cinza, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imagem_original, contornos,-1, (0,255,0), 3)
cv2.imshow('Contornos', imagem_original)
cv2.waitKey(0)
cv2.destroyAllWindows()