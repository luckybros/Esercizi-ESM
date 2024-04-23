#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 14:12:44 2024

@author: luketto
"""
import numpy as np              # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi     # importa Scipy per le immagini
import skimage.io as io         # importa il modulo Input/Output di SK-Image

x = io.imread("dorian.jpg")
(M,N) = x.shape   
xmed = np.mean(x)
xstd = np.std(x)
var  = np.var(x)

MED = np.zeros((M-2,N-2))
for i in range(M-2):
    for j in range(N-2):
        MED[i,j] = np.mean(x[i:i+3,j:j+3])
            
plt.figure() 
plt.imshow(MED, clim=None, cmap="gray")

# con generic filter

y = ndi.generic_filter(x, np.mean, (3,3))
plt.figure()
plt.subplot(1,2,1) 
plt.imshow(x, clim=[0,255], cmap="gray")
plt.subplot(1,2,2) 
plt.imshow(y, clim=[0,255], cmap="gray");

n, b = np.histogram(x, np.arange(257))  # istogramma
plt.figure; plt.bar(np.arange(256), n)  # grafico a barre
plt.axis([0,255,0,1.1*np.max(n)])       # estremi per ascisse e ordinate

