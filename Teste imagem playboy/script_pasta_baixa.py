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

# ============================================
# 2. TRANSFORMADA DE FOURIER
# ============================================

f = np.fft.fft2(img)

# Centralizar frequências
fshift = np.fft.fftshift(f)

# ============================================
# 3. CRIAR FILTRO PASSA-BAIXA
# ============================================

rows, cols = img.shape

crow, ccol = rows // 2, cols // 2

# Máscara inicialmente preta
mask = np.zeros((rows, cols), np.uint8)

# Criar círculo branco no centro
raio = 30

for i in range(rows):
    for j in range(cols):

        if (i - crow)**2 + (j - ccol)**2 <= raio**2:
            mask[i, j] = 1

# ============================================
# 4. APLICAR FILTRO
# ============================================

fshift_filtrado = fshift * mask

# ============================================
# 5. TRANSFORMADA INVERSA
# ============================================

# Desfazer centralização
f_ishift = np.fft.ifftshift(fshift_filtrado)

# Fourier inversa
img_back = np.fft.ifft2(f_ishift)

# Valor absoluto
img_back = np.abs(img_back)

# ============================================
# 6. ESPECTROS
# ============================================

espectro_original = 20 * np.log(np.abs(fshift) + 1)

espectro_filtrado = 20 * np.log(np.abs(fshift_filtrado) + 1)

# ============================================
# 7. MOSTRAR RESULTADOS
# ============================================

plt.figure(figsize=(12,8))

# Imagem original
plt.subplot(221)
plt.imshow(img, cmap='gray')
plt.title('Imagem Original')
plt.axis('off')

# Espectro original
plt.subplot(222)
plt.imshow(espectro_original, cmap='gray')
plt.title('Espectro de Fourier')
plt.axis('off')

# Máscara
plt.subplot(223)
plt.imshow(mask, cmap='gray')
plt.title('Filtro Passa-Baixa')
plt.axis('off')

# Resultado final
plt.subplot(224)
plt.imshow(img_back, cmap='gray')
plt.title('Imagem Filtrada')
plt.axis('off')

plt.tight_layout()
plt.show()