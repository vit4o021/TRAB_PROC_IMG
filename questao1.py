import cv2


#Questão 1:
caminho_imagem = 'img\homemaranha.jpg'
imagem_colorida = cv2.imread(caminho_imagem)
cv2.imshow('Homem aranha', imagem_colorida)
cv2.waitKey(0)
cv2.destroyAllWindows()

