#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Negativo
"""

import numpy as np              # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi     # importa Scipy per le immagini
import skimage.io as io         # importa il modulo Input/Output di SK-Imagex

x = np.float32(io.imread("mammografia.jpg"))

y = 255 - x

plt.figure()
plt.subplot(1,2,1) 
plt.imshow(x, clim=[0,255], cmap="gray")
plt.title('Originale')
plt.subplot(1,2,2) 
plt.imshow(y, clim=[0,255], cmap="gray");
plt.title('Negativo')