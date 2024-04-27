#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Operazioni aritmetche
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

x = io.imread("frattale.jpg")

y = x

for i in range(4):
    y = bit.bitset(y, i, 0)
    
z = x - y

plt.figure()
plt.imshow(z, clim=None, cmap="gray")



