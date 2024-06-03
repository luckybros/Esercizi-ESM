#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Esercizio 2.1.3
Enhancement locale. Si consideri l’immagine bebe.jpg, che rappresenta una 
vecchia fotografia di un neonato, in cui sono presenti dei difetti dovuti al 
passare del tempo. Si vuole realizzare un algoritmo iterativo che effettui 
l’enhancement locale dell’immagine, riguardante cio`e le sole parti 
danneggiate, individuate dalla maschera binaria mask.bmp.
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

def enhanc(x,mask,k):
    x_1 = (x*mask)              # ottengo l'immagine senza rumore
    not_mask = 1 - mask
    a = 0.073
    b = 0.177
    h = np.array([[a, b, a],
                 [b, 0, b],
                 [a, b, a]], dtype=np.float64)
    x_k_1 = x
    for i in range (k):
        x_k = ndi.correlate(x_k_1, h)
        x_filt = x_k*not_mask
        x_k_1 = x_1 + x_filt
    return x_k_1
                    
        
x = ml.leggiJPG("bebe.jpg")
mask = io.imread("mask.bmp")

# Lista dei valori di k 
list_k = [10, 50, 100]

# Crea una figura per mostrare tutte le immagini filtrate
fig, axes = plt.subplots(1, len(list_k), figsize=(15, 5))


for i in range(len(list_k)):
    y = enhanc(x, mask, list_k[i])
    axes[i].imshow(y, cmap='gray')
    axes[i].set_title(f"filtrata per k = {list_k[i]}")
    axes[i].axis('off')  # Rimuove gli assi

# Mostra la figura con tutte le immagini filtrate
plt.tight_layout()
plt.show()






