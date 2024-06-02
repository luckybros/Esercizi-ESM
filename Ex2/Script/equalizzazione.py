#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Equalizzazione
"""

import numpy as np              # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi     # importa Scipy per le immagini
import skimage.io as io         # importa il modulo Input/Output di SK-Imagex
import skimage.exposure as ex

x = io.imread("marte.jpg")

n, b = np.histogram(x, np.arange(257))  # istogramma

plt.figure()
plt.bar(np.arange(256), n)
plt.axis([0,255,0,1.1*np.max(n)])
plt.title('Istogramma di marte.jpg')

y = ex.equalize_hist(x)
y = 255*y

ny, by = np.histogram(y, np.arange(257))  # istogramma

plt.figure()
plt.bar(np.arange(256), ny)
plt.axis([0,255,0,1.1*np.max(ny)])
plt.title('Istogramma di marte.jpg dopo equalizzazione')


