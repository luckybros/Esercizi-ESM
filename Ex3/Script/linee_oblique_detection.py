#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Maschere oblique
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

x = ml.leggiJPG("angiogramma.jpg")
h = np.array([[0,1,2],[-1,0,1],[-2,-1,0]], dtype=np.float64)
z = ndi.correlate(x, h)
sigma = 5
y0 = ndi.gaussian_filter(z, (sigma,sigma))

ml.showTwoImages(x, y0, "originale", "filtrata (gaussiano)")

y1 = ml.smooth_media_aritmetica(z, sigma)

ml.showTwoImages(x, y1, "originale", "filtrata (media aritmetica)")