#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

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

k = 20
x = ml.leggiJPG("test.jpg")
h = np.array([[1,0,-1],[2,0,-2],[1,0,-1]], dtype=np.float64)    # filtro di sobel
#h = np.ones((k,k))/(k^2)

M,N = x.shape
A,B = h.shape
P = M + A -1
Q = N + B -1
X = np.fft.fft2(x, (P,Q))
H = np.fft.fft2(h, (P,Q))
Y=H*X
y = np.real(np.fft.ifft2(Y))    # l'antitrasformata dovrebbe essere puramente reale, ma errori dovuti
                                # alla precisione comportano che l'antitrasformata abbia una piccola parte
                                # immaginaria
ml.showImage(y, "ciao")
