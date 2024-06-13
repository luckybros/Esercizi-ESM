#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 18:46:48 2024

@author: luketto
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

x = ml.leggiJPG("lena.jpg")
M,N = x.shape
m = np.fft.fftshift(np.fft.fftfreq(M))
n = np.fft.fftshift(np.fft.fftfreq(N))
l,k = np.meshgrid(n,m)
D = np.sqrt(k**2+l**2)
D0 = 0.1;
H =(D<=D0)
plt.figure();
plt.imshow(H, clim=[0,1], cmap="gray", extent=(-0.5,+0.5,+0.5,-0.5));   # filtro tra 0 ed 1 di colori, in grigio
plt.title("Filtro passa alto")

X = np.fft.fft2(x)
X = np.fft.fftshift(X)
plt.figure()
plt.imshow(np.log(1 + np.abs(X)), clim=None, cmap="gray", extent=(-0.5,+0.5,+0.5,-0.5));
plt.title("Trasformata dell'ingresso")

Y = H*X
plt.figure()
plt.imshow(np.log(1 + np.abs(Y)), clim=None, cmap = "gray", extent=(-0.5,+0.5,+0.5,-0.5));
plt.title("Trasformata dell'uscita")

Y = np.fft.ifftshift(Y)
y = np.real(np.fft.ifft2(Y))
plt.figure()
plt.imshow(y, clim=[0,255], cmap="gray")
plt.title("Uscita")


