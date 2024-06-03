#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Esercizio 2.1.4
Filtri direzionali. Allo scopo di migliorare il filtraggio di immagini 
rumorose si vogliono utilizzare filtri direzionali. In particolare, 
considerate le seguenti maschere 9 × 9 per il filtraggio:

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

x = np.fromfile('zebre.y', np.uint8)
x = np.reshape(x, (321, 481))

masks = np.array([
    [
        [1, 1, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 1]
    ],
    [
        [0, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0]
    ],
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ],
    [
        [0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0]
    ]
])

n = 25*np.random.randn(*x.shape)
x_noisy = x + n

local_variances = []
# per accedere, masks['mask_1']
for i in range(len(masks)):
    local_variances.append(ndi.generic_filter(x_noisy, np.var, footprint=masks[i]))
    
    
# Creiamo una matrice per memorizzare l'indice della maschera con varianza minima per ciascun pixel
mask_indices = np.zeros_like(x_noisy, dtype=np.uint8)
filtered_image = np.zeros_like(x_noisy)

for i in range(4, x_noisy.shape[0] - 4):
    for j in range(4, x_noisy.shape[1] - 4):
        variances_i_j = [local_variances[k][i][j] for k in range(len(local_variances))]
        min_index = np.argmin(variances_i_j)
        min_mask = masks[min_index]
        filtered_pixel_value = np.sum(min_mask * x_noisy[i-4:i+5, j-4:j+5]) / np.sum(min_mask)
        filtered_image[i][j] = filtered_pixel_value
        
z = ndi.uniform_filter(x, (5, 5))

max_pixel_value = np.max(x)
mse = np.mean((x - filtered_image) ** 2)
psnr = 10 * np.log10((max_pixel_value ** 2) / mse)

ml.showTwoImages(z, filtered_image, "media", "procedura")
        

        
        
        