#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FSHS
"""

import numpy as np              # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi     # importa Scipy per le immagini
import skimage.io as io         # importa il modulo Input/Output di SK-Imagex

K = 256

def fshs(x): 
    x_max = np.max(x)
    x_min = np.min(x)
    
    a = (K - 1)/(x_max - x_min)
    b = x_min
    
    y = a*(x - b)
    
    return y

    
x = io.imread("granelli.jpg")
n, b = np.histogram(x, np.arange(257))  # istogramma

plt.figure()
plt.bar(np.arange(256), n)
plt.axis([0,255,0,1.1*np.max(n)])
plt.title('Istogramma di granelli.jpg')

y = fshs(x)
ny, by = np.histogram(y, np.arange(257))  # istogramma

plt.figure()
plt.bar(np.arange(256), ny)
plt.axis([0,255,0,1.1*np.max(ny)])
plt.title('Istogramma di granelli.jpg dopo FSHS')



