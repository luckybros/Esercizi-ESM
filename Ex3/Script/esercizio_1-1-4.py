#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Esercizio 1.1.4
Filtraggio spaziale adattativo
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

def filtra(x, sigma):
    var = sigma**2
    mu_l = ndi.generic_filter(x, np.mean, (7,7))
    var_l = ndi.generic_filter(x, np.var, (7,7))
    
    """
    mu_l = ndi.uniform_filter(x, (7,7))
    var_l = ndi.generic_filter(x**2,, (7,7)) - mu_l
    """
    y = x - ((var/var_l)*(x - mu_l))
    return y
       
x = ml.leggiJPG("lena.jpg")
M,N = x.shape
ml.showImage(x, "orginale")

sigma = [5,10,15,20,25,30,35]
mse_noisy = np.zeros(len(sigma))
mse_media = np.zeros(len(sigma))
mse_adatt = np.zeros(len(sigma))

for i in range (len(sigma)):
    n = (sigma[i]**2)*np.random.randn(M,N)
    y = x + n
    z = filtra(y, sigma[i])
    z_media = ndi.generic_filter(x, np.mean, (7,7))
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
