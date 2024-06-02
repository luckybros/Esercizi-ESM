#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bit-place slicing
"""
import sys
sys.path.append('/Users/luketto/Desktop/II Semestre IV Anno/ESM/Esercizi/Librerie')
import MyLibrary as ml
from bitop import bitget
import numpy as np              # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi     # importa Scipy per le immagini
import skimage.io as io         # importa il modulo Input/Output di SK-Imagex
import skimage.exposure as ex

x = io.imread("frattale.jpg")

M, N = x.shape
bitplane = np.zeros((M,N,8), dtype=bool)  # matrice 3D

for i in range(8):
    bitplane[:, :, i] = bitget(x, i)

# Mostra tutti i bitplane in una singola figura
plt.figure(figsize=(12, 6))  # imposta la dimensione della figura
for i in range(8):
    plt.subplot(2, 4, i + 1)  # crea una griglia 2x4 per i subplot
    plt.imshow(bitplane[:, :, i], clim=[0, 1], cmap="gray")
    plt.title("Bitplane %d" % i)
    plt.axis('off')  # nasconde gli assi per una visualizzazione più pulita

plt.tight_layout()  # regola automaticamente i layout per prevenire sovrapposizioni
plt.show()
