# Atividade para Compor B2 — Filtros de Imagem

Aplicação prática de filtros de processamento de imagem (Média, Mediana e Sobel) utilizando Python e OpenCV.

---

## 📋 Descrição

Este projeto consiste em carregar uma imagem, aplicar três tipos de filtros clássicos de processamento digital de imagens e analisar os efeitos produzidos por cada um deles.

---

## 🚀 Etapas da Atividade

### 1. Carregar uma Imagem
Carregue uma imagem de sua escolha para ser usada como base nos experimentos.

### 2. Aplicar os Filtros

Aplique os seguintes filtros sobre a imagem original e observe as mudanças:

- **Filtro de Média** — suaviza a imagem calculando a média dos pixels vizinhos.
- **Filtro de Mediana** — suaviza a imagem substituindo cada pixel pela mediana da vizinhança.
- **Filtro de Sobel** — detecta bordas calculando o gradiente da intensidade dos pixels.

### 3. Analisar os Resultados

Responda às perguntas a seguir com base nas observações.

### 4. Experimentar

Teste diferentes tamanhos de kernel nos filtros de Média e Mediana — por exemplo, `(3, 3)`, `(5, 5)`, `(7, 7)` — e observe como o tamanho afeta a suavização da imagem.

---

## 💻 Exemplo de Código (Python + OpenCV)

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Carregar imagem
img = cv2.imread('imagem.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 2. Aplicar filtros
media    = cv2.blur(img_rgb, (5, 5))
mediana  = cv2.medianBlur(img_rgb, 5)
sobel_x  = cv2.Sobel(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), cv2.CV_64F, 1, 0, ksize=3)
sobel_y  = cv2.Sobel(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), cv2.CV_64F, 0, 1, ksize=3)
sobel    = cv2.magnitude(sobel_x, sobel_y)

# 3. Visualizar resultados
titulos  = ['Original', 'Média (5x5)', 'Mediana (5x5)', 'Sobel']
imagens  = [img_rgb, media, mediana, sobel]

fig, axs = plt.subplots(1, 4, figsize=(18, 5))
for ax, titulo, imagem in zip(axs, titulos, imagens):
    ax.imshow(imagem, cmap='gray' if titulo == 'Sobel' else None)
    ax.set_title(titulo)
    ax.axis('off')
plt.tight_layout()
plt.show()
```

---

## ❓ Perguntas e Respostas

### a) Como a imagem original mudou após a aplicação de cada filtro?

| Filtro | Efeito na Imagem |
|--------|-----------------|
| **Média** | A imagem ficou visivelmente borrada/suavizada. Detalhes finos e texturas são reduzidos porque cada pixel passa a representar a média dos seus vizinhos, diluindo diferenças abruptas de intensidade. |
| **Mediana** | A imagem também ficou suavizada, porém preservando melhor as bordas do que o filtro de média. Ruídos do tipo "sal e pimenta" foram eliminados de forma eficaz, pois a mediana ignora valores extremos. |
| **Sobel** | A imagem foi transformada em um mapa de bordas. As regiões com grande variação de intensidade (contornos e transições) foram realçadas em branco/cinza claro, enquanto regiões homogêneas ficaram escuras. |

---

### b) Qual filtro foi mais eficaz para suavizar a imagem?

O **Filtro de Mediana** é, em geral, o mais eficaz para suavização com preservação de qualidade, pois:

- Remove ruídos impulsivos (sal e pimenta) sem borrar as bordas.
- O **Filtro de Média** também suaviza, porém de forma menos seletiva — ele borra tanto o ruído quanto as bordas, resultando em uma imagem mais "embaçada".

Para suavização simples sem preocupação com bordas, o filtro de média é suficiente. Para maior qualidade visual, o filtro de mediana é preferido.

---

### c) Qual filtro foi mais eficaz para destacar as bordas?

O **Filtro de Sobel** foi o mais eficaz para destacar bordas. Ele calcula o gradiente da intensidade da imagem nas direções horizontal e vertical, produzindo uma resposta forte onde há transições abruptas de intensidade — que correspondem exatamente às bordas dos objetos.

Os filtros de média e mediana, por serem filtros de suavização, fazem o oposto: reduzem bordas em vez de destacá-las.

---

### d) Quais situações podem exigir o uso de cada tipo de filtro em um projeto real?

| Filtro | Quando Usar |
|--------|------------|
| **Média** | Redução de ruído gaussiano em imagens capturadas em baixa luminosidade; pré-processamento rápido quando a preservação de bordas não é crítica; compressão de detalhes antes de operações de visão computacional simples. |
| **Mediana** | Remoção de ruído sal e pimenta em imagens médicas (raio-X, ultrassom) ou capturadas por sensores defeituosos; pré-processamento de imagens para OCR (reconhecimento de texto), onde bordas nítidas são importantes; fotografia digital e restauração de imagens antigas. |
| **Sobel** | Detecção de objetos e segmentação em sistemas de visão computacional e robótica; reconhecimento de padrões e formas; pré-processamento para algoritmos de machine learning que utilizam contornos como features; inspeção industrial automatizada para detectar defeitos em superfícies. |

---

## 🔬 Experimento com Diferentes Tamanhos de Kernel

```python
kernels = [3, 5, 7, 11]

fig, axs = plt.subplots(2, len(kernels), figsize=(18, 8))

for i, k in enumerate(kernels):
    media_k   = cv2.blur(img_rgb, (k, k))
    mediana_k = cv2.medianBlur(img_rgb, k)

    axs[0, i].imshow(media_k)
    axs[0, i].set_title(f'Média ({k}x{k})')
    axs[0, i].axis('off')

    axs[1, i].imshow(mediana_k)
    axs[1, i].set_title(f'Mediana ({k}x{k})')
    axs[1, i].axis('off')

plt.suptitle('Efeito do Tamanho do Kernel na Suavização', fontsize=14)
plt.tight_layout()
plt.show()
```

**Conclusão do experimento:** Quanto maior o kernel, maior a área de vizinhança considerada por cada pixel, resultando em uma suavização mais intensa. Kernels pequenos (3×3) produzem suavização sutil; kernels grandes (11×11 ou mais) produzem um forte efeito de borrão, podendo eliminar detalhes importantes da imagem.

---

## 🛠️ Dependências

```bash
pip install opencv-python numpy matplotlib
```

---

## 📁 Estrutura do Projeto

```
projeto-filtros/
├── imagem.jpg          # Imagem de entrada
├── main.py             # Script principal
└── README.md           # Este arquivo
```
