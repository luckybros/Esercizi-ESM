#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Edge detection basata sul gradiente
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

x = ml.leggiRAW("house.y", 512, 512, np.int8)

sobel_mask = np.array([[-1,-2,-1],[0,0,0],[-1,-2,-1]], dtype=np.float64)

y = ndi.correlate(x, sobel_mask)

T = 1.5*np.mean(y)

z = ml.thresholding(y, T)

ml.show_three_images(x, "originale", y, "gradiente", z, "contorni")