import cv2
import matplotlib.pyplot as plt

# Carregar imagem
imagem = cv2.imread("imagem.jpg")

# Converter BGR para RGB
imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

# =========================
# FILTRO MÉDIA KERNEL 3x3
# =========================
media_3x3 = cv2.blur(imagem_rgb, (3, 3))

# =========================
# FILTRO MÉDIA KERNEL 5x5
# =========================
media_5x5 = cv2.blur(imagem_rgb, (5, 5))

# Mostrar imagens
plt.figure(figsize=(12, 6))

# Original
plt.subplot(1, 3, 1)
plt.imshow(imagem_rgb)
plt.title("Original")
plt.axis("off")

# Kernel 3x3
plt.subplot(1, 3, 2)
plt.imshow(media_3x3)
plt.title("Kernel 3x3")
plt.axis("off")

# Kernel 5x5
plt.subplot(1, 3, 3)
plt.imshow(media_5x5)
plt.title("Kernel 5x5")
plt.axis("off")

plt.show()