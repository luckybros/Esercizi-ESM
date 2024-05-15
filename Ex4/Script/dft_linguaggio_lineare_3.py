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
D = np.sqrt(k**2+ l**2)
D0 = 0.1;
H =(D<=D0)
plt.figure();
plt.imshow(H, clim=[0,1], cmap="gray", extent=(-0.5,+0.5,+0.5,-0.5));

X = np.fft.fft2(x)
X = np.fft.fftshift(X)
X = np.log(1 + np.abs(X))
plt.imshow(X, clim=[0,1], cmap="gray", extent=(-0.5,+0.5,+0.5,-0.5));

Y = H*X
Y = np.log(1 + np.abs(Y))
plt.imshow(Y, clim=[0,1], cmap="gray", extent=(-0.5,+0.5,+0.5,-0.5));

Y = np.fft.ifftshift(Y)
y = np.real(np.fft.ifft2(Y))
ml.showImage(y, "lena ricostruita")


