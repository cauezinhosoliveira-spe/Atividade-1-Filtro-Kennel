# 🖼️ Atividade para Compor B2 — Filtros de Imagem

Atividade prática de processamento de imagens com aplicação e análise de filtros clássicos de visão computacional.

---

## 📋 Descrição

Este projeto tem como objetivo carregar uma imagem e aplicar diferentes filtros de processamento — **média**, **mediana** e **Sobel** — observando e comparando os efeitos de cada um sobre a imagem original.

---

## 🚀 Etapas da Atividade

### 1. Carregar uma Imagem
Selecione uma imagem de entrada para ser processada nas etapas seguintes.

### 2. Aplicar os Filtros
Aplique os seguintes filtros sobre a imagem original e observe as mudanças:

| Filtro   | Efeito Principal                        |
|----------|-----------------------------------------|
| Média    | Suavização (blur) por média dos pixels  |
| Mediana  | Suavização com preservação de bordas    |
| Sobel    | Detecção e destaque de bordas           |

### 3. Analisar os Resultados
Responda às seguintes perguntas após a aplicação dos filtros:

- **a)** Como a imagem original mudou após a aplicação de cada filtro?
- **b)** Qual filtro foi mais eficaz para **suavizar** a imagem?
- **c)** Qual filtro foi mais eficaz para **destacar as bordas**?
- **d)** Quais situações podem exigir o uso de cada tipo de filtro em um projeto real?

### 4. Experimentar
Teste diferentes tamanhos de kernel nos filtros de média e mediana — por exemplo, `(3, 3)`, `(5, 5)` — e observe como isso afeta a suavização da imagem.

---

## 🛠️ Tecnologias Sugeridas

- **Python 3.x**
- **OpenCV** (`cv2`) — aplicação dos filtros
- **NumPy** — manipulação de arrays de imagem
- **Matplotlib** — visualização e comparação dos resultados

### Instalação das dependências

```bash
pip install opencv-python numpy matplotlib
```

---

## 💻 Exemplo de Código

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Carregar a imagem
imagem = cv2.imread('imagem.jpg')
imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

# 2. Aplicar os filtros
filtro_media   = cv2.blur(imagem_rgb, (5, 5))
filtro_mediana = cv2.medianBlur(imagem_rgb, 5)
filtro_sobel_x = cv2.Sobel(imagem_rgb, cv2.CV_64F, 1, 0, ksize=3)
filtro_sobel_y = cv2.Sobel(imagem_rgb, cv2.CV_64F, 0, 1, ksize=3)
filtro_sobel   = cv2.magnitude(filtro_sobel_x, filtro_sobel_y)

# 3. Visualizar os resultados
titulos  = ['Original', 'Média', 'Mediana', 'Sobel']
imagens  = [imagem_rgb, filtro_media, filtro_mediana, filtro_sobel]

fig, axes = plt.subplots(1, 4, figsize=(20, 5))
for ax, img, titulo in zip(axes, imagens, titulos):
    ax.imshow(img.astype(np.uint8))
    ax.set_title(titulo)
    ax.axis('off')

plt.tight_layout()
plt.show()
```

---

## 🔬 Experimentos com Diferentes Kernels

```python
kernels = [(3, 3), (5, 5), (7, 7)]

for k in kernels:
    media   = cv2.blur(imagem_rgb, k)
    mediana = cv2.medianBlur(imagem_rgb, k[0])
    print(f"Kernel {k}: filtros aplicados com sucesso.")
```

---

## 📊 Análise Esperada

| Filtro   | Suavização | Detecção de Bordas | Sensível a Ruído |
|----------|------------|-------------------|-----------------|
| Média    | ✅ Alta     | ❌ Não             | ⚠️ Sim           |
| Mediana  | ✅ Alta     | ❌ Não             | ✅ Não (robusto) |
| Sobel    | ❌ Não      | ✅ Alta            | ⚠️ Sim           |

---

## 📝 Conclusões

Ao final da atividade, espera-se que o aluno seja capaz de:

- Distinguir os efeitos visuais de cada filtro
- Identificar o filtro adequado para cada tipo de problema (remoção de ruído vs. detecção de contornos)
- Compreender a influência do tamanho do kernel na intensidade do efeito aplicado

---

## 📁 Estrutura Sugerida do Projeto

```
b2-filtros-imagem/
├── imagem.jpg          # Imagem de entrada
├── filtros.py          # Script principal
├── resultados/         # Imagens geradas
│   ├── media.jpg
│   ├── mediana.jpg
│   └── sobel.jpg
└── README.md
```
