#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 15:32:42 2024

@author: luketto
"""
import numpy as np              # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi     # importa Scipy per le immagini
import skimage.io as io         # importa il modulo Input/Output di SK-Image

x = io.imread("vista_aerea.jpg")

n, b = np.histogram(x, np.arange(257))  # istogramma
             
y = x - 50

mask = y<0     # crea una matrice di vero (True) e falso (False)
y[mask] = 0    # si annullano tutti i valori minori di 0

y[y > 255] = 0   # si annullano tutti i valori superiori a 255

ny, by = np.histogram(y, np.arange(257))  # istogramma

plt.figure()
plt.subplot(1,2,1) 
plt.imshow(x, clim=[0,255], cmap="gray")
plt.subplot(1,2,2) 
plt.imshow(y, clim=[0,255], cmap="gray");

plt.figure()
plt.subplot(1,2,1) 
plt.bar(np.arange(256), n)
plt.axis([0,255,0,1.1*np.max(n)])
plt.title('Istogramma di vista_area.jpg')
plt.subplot(1,2,2) 
plt.bar(np.arange(256), ny)
plt.axis([0,255,0,1.1*np.max(ny)])
plt.title('Istogramma traslato di vista_area.jpg')
