#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Grafico 3D
"""

import sys
sys.path.append('/Users/luketto/Desktop/II Semestre IV Anno/ESM/Esercizi/Librerie')
import MyLibrary as ml
import numpy as np              # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi     # importa Scipy per le immagini
import skimage.io as io         # importa il modulo Input/Output di SK-Imagex
import skimage.exposure as ex
import skimage.color as col
import scipy.ndimage as ndi
from mpl_toolkits.mplot3d import Axes3D

x = ml.leggiJPG("rettangolo.jpg")

M,N = x.shape
P = 2*M; Q = 2*N
X = np.fft.fft2(x, (P,Q))

Y = np.log(1+np.abs((np.fft.fftshift(X))))

m = np.fft.fftshift(np.fft.fftfreq(Y.shape[0]))
n = np.fft.fftshift(np.fft.fftfreq(Y.shape[1]))

ax = plt.figure().add_subplot(projection='3d')
l,k = np.meshgrid(n,m)
ax.plot_surface(l,k,Y, linewidth=0, cmap="jet")
