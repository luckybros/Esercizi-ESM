#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Zero padding
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
M,N = x.shape
P = 2*M; Q = 2*N
X = np.fft.fft2(x, (P,Q))
X = np.abs(X)
X = np.log(1 + X)
Y = np.fft.fft2(x)
Y = np.abs(Y)
Y = np.log(1 + Y)
ml.showTwoImages(X, Y, "con padding", "normale")

