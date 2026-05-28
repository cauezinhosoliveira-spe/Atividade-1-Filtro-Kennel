import cv2

# carregar imagem
img = cv2.imread("milho.jpg")

# inverter imagem
invertida = 255 - img

# mostrar
cv2.imshow("Original", img)
cv2.imshow("Invertida", invertida)

cv2.waitkey(0)
cv2.destroyAllWindows()