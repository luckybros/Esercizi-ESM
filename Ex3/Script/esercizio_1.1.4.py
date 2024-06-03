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
M,N = x.shape
ml.showImage(x, "orginale")
var = np.var(x)

def filtra(b): 
    b = np.reshape(b, (7,7))
    mu_l = np.mean(b)
    var_l = np.var(b)
    
    y = b[3][3]
    
    if var_l == 0:
        return y 
    
    return (y - (var/var_l)*(y - mu_l))

sigma = [5,10,15,20,25,30,35]
mse_noisy = np.zeros(len(sigma))
mse_media = np.zeros(len(sigma))
mse_adatt = np.zeros(len(sigma))

for i in range (len(sigma)):
    n = (sigma[i])*np.random.randn(M,N)
    y = x + n
    z = ndi.generic_filter(y, filtra, (7,7))
    z_media = ndi.generic_filter(y, np.mean, (7,7))
    mse_noisy[i] = np.mean((x - y) **2)
    mse_media[i] = np.mean((x - z_media) **2)
    mse_adatt[i] = np.mean((x - z) **2)
    
plt.figure()
plt.plot(sigma, mse_noisy, 'r-*', label='Noisy')
plt.plot(sigma, mse_media, 'g-o', label='Media')
plt.plot(sigma, mse_adatt, 'b-x', label='Adattativo')
plt.xlabel("Sigma")
plt.ylabel("MSE")
plt.legend()
plt.show()
    
    
    
    
    
    
    
    
    
    