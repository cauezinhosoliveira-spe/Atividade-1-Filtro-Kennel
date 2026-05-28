import cv2

# carregar imagem em tons de cinza
img = cv2.imread('raiox.jpg', 0)

# aplicar limiar (_, resultado = retorno, imagem_processada)
_, resultado = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

cv2.imshow('Original', img)
cv2.imshow('Limiar', resultado)

cv2.waitKey(0)
cv2.destroyAllWindows()