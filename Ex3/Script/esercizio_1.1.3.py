#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Esercizio 1.1.3
Denoising. Aggiungete del rumore gaussiano bianco ad un immagine x con il comando: 
noisy = x + n con n = d*np.random.randn(M,N) dove d è la deviazione standard del 
rumore. Effettuate il denoising dell’immagine con i filtri a media mobile 
(al variare della dimensione della finestra). Valutate l’efficacia del filtraggio 
sia visivamente, sia calcolando l’errore quadratico medio tra x e l’immagine 
"ripulita”, che rappresenta una misura quantitativa per stabilire quanto 
l’immagine elaborata sia simile all’originale. L’MSE (Mean Squared Error) 
tra due immagini si definisce come:
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

x = ml.leggiJPG("lena.jpg")
(M,N) = x.shape

ml.showImage(x, "orginale")
n = 20*np.random.randn(M,N)

noisy = x + n

ml.showImage(noisy, "rumorosa")

list_k = [3, 5, 7, 9, 11, 13, 15]
mse = np.zeros(len(list_k))

for i in range(len(list_k)):
    y = ml.smooth_media_aritmetica(noisy, list_k[i])
    ml.showImage(y, "filtrata per k = %d" %list_k[i])
    mse[i] = np.mean((x - y) **2)
    
plt.figure();
plt.plot(list_k,mse,"r-*");
plt.xlabel("dimensione della finestra");
plt.ylabel("MSE");
    

