import sys
sys.path.append('/Users/luketto/Desktop/II Semestre IV Anno/ESM/Esercizi/Librerie')
import MyLibrary as ml
import bitop as bit
import numpy as np              # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi     # importa Scipy per le immagini
import skimage.io as io         # importa il modulo Input/Output di SK-Imagex
import skimage.exposure as ex
import skimage.color as col
import scipy.ndimage as ndi
import skimage.color.rgb2hsv as rgb2hsv
import skimage.color.hsv2rgb as hsv2rgb

# Lettura e normalizzazione dell'immagine
x = io.imread('colori.jpg')
x = np.float64(x) / 255

# Visualizzazione dell'immagine originale
plt.figure(1)
plt.imshow(x)
plt.title('Immagine originale')

# Definizione del valore gamma
gamma = 0.6

# Elaborazione in RGB
y = x ** gamma
plt.figure(2)
plt.imshow(y)
plt.title('Elaborazione in RGB')

# Elaborazione in HSI
w = rgb2hsv(x)
w[:, :, 2] = w[:, :, 2] ** gamma
z = hsv2rgb(w)
plt.figure(3)
plt.imshow(z)
plt.title('Elaborazione in HSI')

# Mostra tutte le figure
plt.show()

