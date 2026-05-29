import cv2
import matplotlib.pyplot as plt

# Carregar imagem
imagem = cv2.imread("imagem.jpg")

# Converter BGR para RGB
imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

# Aplicar filtro de média
media = cv2.blur(imagem_rgb, (5, 5))

# Aplicar filtro de mediana
mediana = cv2.medianBlur(imagem_rgb, 5)

# Aplicar filtro Sobel
sobel_x = cv2.Sobel(imagem_rgb, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(imagem_rgb, cv2.CV_64F, 0, 1, ksize=3)
sobel = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

# Mostrar imagens
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(imagem_rgb)
plt.title("Imagem Original")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(media)
plt.title("Filtro de Média")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(mediana)
plt.title("Filtro de Mediana")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(sobel.astype("uint8"))
plt.title("Filtro Sobel")
plt.axis("off")

plt.show()