#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Trasformata discreta 2-D
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
import skimage.color as col
import scipy.ndimage as ndi

x = ml.leggiJPG("rettangolo.jpg")

X = np.fft.fft2(x)
X = np.abs(X)

ml.showTwoImages(x, X, "Normale", "Trasformata")

Y = np.log(1+np.abs(np.fft.fftshift(X)))
plt.figure();
plt.imshow(Y, clim=None, cmap="gray", extent=(-0.5,+0.5,+0.5,-0.5));