#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 00:25:36 2024

@author: luketto
"""

import numpy as np              # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi     # importa Scipy per le immagini
import skimage.io as io         # importa il modulo Input/Output di SK-Image

x = io.imread("fragole.jpg")
plt.figure()
plt.imshow(x)

R = x[:,:,0]
#plt.figure()
#plt.imshow(R, clim=None, cmap="gray")
#plt.title("componente di rosso")

G = x[:,:,1]
#plt.figure();
#plt.imshow(G, clim=None, cmap="gray");
#plt.title("componente di verde");

B = x[:,:,2]
#plt.figure()
#plt.imshow(B, clim=None, cmap="gray")
#plt.title("componente di blu")

# Annulliamo la componente di rosso e ricostruiamo l'immagine
M = x.shape[0]
N = x.shape[1]
R_zeroes = np.zeros((M,N), x.dtype)
y = np.stack((R_zeroes, G, B), -1)
plt.figure()
plt.imshow(y, clim=None, cmap="gray")
plt.title("annullamento componente di rosso")