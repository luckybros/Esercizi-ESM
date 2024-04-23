#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Statistiche locali
"""

import numpy as np              # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi     # importa Scipy per le immagini
import skimage.io as io         # importa il modulo Input/Output di SK-Imagex

E = 4
k0 = 0.4
k1 = 0.02
k2 = 0.4

x = np.float32(io.imread("filamento.jpg"))

mu_x = np.mean(x)
sigma_x = np.std(x)

mu_l = ndi.generic_filter(x, np.mean, (3,3))
sigma_l = ndi.generic_filter(x, np.var, (3,3))

mask = ((mu_l <= k0*mu_x) & (k1*sigma_x <= sigma_l) & (sigma_l <= k2*sigma_x))

y = x + E*x*mask

plt.figure()
plt.subplot(1,2,1) 
plt.imshow(x, clim=[0,255], cmap="gray")
plt.title('Originale')
plt.subplot(1,2,2) 
plt.imshow(y, clim=[0,255], cmap="gray");
plt.title('Modificato')