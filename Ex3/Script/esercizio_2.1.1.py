#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Esercizio 2.1.1
Rumore sale e pepe. Scegliete un’immagine, quindi aggiungete rumore sale e pepe 
(usate la funzione skimage.util.random noise), applicate il filtro mediano e 
valutate il risultato sia visivamente sia tramite l’errore quadratico medio 
se la dimensione della finestra `e 5, 7, 9.
"""
import sys
sys.path.append('/Users/luketto/Desktop/II Semestre IV Anno/ESM/Esercizi/Librerie')
import MyLibrary as ml
import bitop as bit
import numpy as np              # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi     # importa Scipy per le immagini
import skimage.io as io         # importa il modulo Input/Output di SK-Imagex
import skimage.exposure as ex
import scipy.ndimage as ndi
import skimage.util as uti

x = ml.leggiJPG("lena.jpg")
(M, N) = x.shape
n = 20 * np.random.randn(M, N)
x_noisy = x + n
ml.showImage(x_noisy, "rumorosa")

list_k = [5, 7, 9]
mse = np.zeros(len(list_k))

y = ndi.median_filter(x, (5,5))

# Crea una figura per mostrare tutte le immagini filtrate
fig, axes = plt.subplots(1, len(list_k), figsize=(15, 5))

for i in range(len(list_k)):
    y = ndi.median_filter(x_noisy, (list_k[i],list_k[i]))
    axes[i].imshow(y, cmap='gray')
    axes[i].set_title(f"filtrata per k = {list_k[i]}")
    axes[i].axis('off')  # Rimuove gli assi
    mse[i] = np.mean((x_noisy - y) ** 2)
    
# Mostra la figura con tutte le immagini filtrate
plt.tight_layout()
plt.show()

# Traccia il grafico MSE
plt.figure()
plt.plot(list_k, mse, "r-*")
plt.xlabel("dimensione della finestra")
plt.ylabel("MSE")
plt.show()    
    
    
    
    
    