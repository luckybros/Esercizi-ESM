#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Uso della DFT per il filtraggio lineare
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

x = np.array([1,2,3,4], dtype=np.float64)
h = np.array([1,1,1]  , dtype=np.float64)

X = np.fft.fft(x,6)
H = np.fft.fft(h,6)

Y=X*H
y = np.real(np.fft.ifft(Y,6))
y_conv = np.convolve(x,h)

print(y)
print(y_conv)
