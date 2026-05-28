import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# ==========================================================
# 1. CARREGAR IMAGEM
# ==========================================================

# Garante que o caminho é relativo ao próprio script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
img = cv2.imread(os.path.join(BASE_DIR, 'lena.png'), 0)

# Verificar se carregou corretamente
if img is None:
    print("Erro ao carregar imagem.")
    exit()

# ==========================================================
# 2. ADICIONAR RUÍDO PERIÓDICO (LINHAS DIAGONAIS)
# ==========================================================

rows, cols = img.shape

# Criar padrão senoidal diagonal
x = np.arange(cols)
y = np.arange(rows)

X, Y = np.meshgrid(x, y)

# Frequência do ruído
frequencia = 0.15

# Ruído periódico
ruido = 50 * np.sin(2 * np.pi * frequencia * (X + Y))

# Adicionar ruído à imagem
img_ruido = img + ruido

# Limitar valores entre 0 e 255
img_ruido = np.clip(img_ruido, 0, 255).astype(np.uint8)

# ==========================================================
# 3. TRANSFORMADA DE FOURIER
# ==========================================================

f = np.fft.fft2(img_ruido)
fshift = np.fft.fftshift(f)

# Espectro da imagem original
magnitude_spectrum = 20 * np.log(np.abs(fshift) + 1)

# ==========================================================
# 4. CRIAR FILTRO NOTCH (REJEITA FAIXA)
# ==========================================================

mask = np.ones((rows, cols), np.uint8)

crow, ccol = rows // 2, cols // 2

# Coordenadas dos ruídos no espectro
# Ajuste dependendo da frequência do ruído
pontos = [
    (crow - 80, ccol - 80),
    (crow - 60, ccol - 60),
    (crow - 40, ccol - 40),
    (crow - 20, ccol - 20),

    (crow + 20, ccol + 20),
    (crow + 40, ccol + 40),
    (crow + 60, ccol + 60),
    (crow + 80, ccol + 80)
]

# Criar buracos no espectro
raio = 8

for ponto in pontos:
    x, y = ponto

    for i in range(rows):
        for j in range(cols):

            if (i - x)**2 + (j - y)**2 <= raio**2:
                mask[i, j] = 0

# ==========================================================
# 5. APLICAR FILTRO
# ==========================================================

fshift_filtrado = fshift * mask

# Espectro filtrado
magnitude_filtrado = 20 * np.log(np.abs(fshift_filtrado) + 1)

# ==========================================================
# 6. TRANSFORMADA INVERSA
# ==========================================================

f_ishift = np.fft.ifftshift(fshift_filtrado)

img_back = np.fft.ifft2(f_ishift)

img_back = np.abs(img_back)

# ==========================================================
# 7. EXIBIR RESULTADOS
# ==========================================================

plt.figure(figsize=(12,10))

# Imagem original com ruído
plt.subplot(221)
plt.imshow(img_ruido, cmap='gray')
plt.title('Imagem Original')
plt.axis('off')

# Imagem final
plt.subplot(222)
plt.imshow(img_back, cmap='gray')
plt.title('Imagem Final')
plt.axis('off')

# Espectro original
plt.subplot(223)
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Espectro da Imagem Original')
plt.axis('off')

# Espectro filtrado
plt.subplot(224)
plt.imshow(magnitude_filtrado, cmap='gray')
plt.title('Espectro da Imagem Final')
plt.axis('off')

plt.tight_layout()
plt.show()