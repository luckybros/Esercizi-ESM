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

def gaussLPF(x, sigma):
    M, N = x.shape
    m = np.fft.fftshift(np.fft.fftfreq(M))
    n = np.fft.fftshift(np.fft.fftfreq(N))
    l, k = np.meshgrid(n, m)
    D = np.sqrt(k**2 + l**2)
    
    H = np.exp(-(D**2) / (2 * sigma**2))  # filtro gaussiano
    
    X = np.fft.fft2(x)
    X = np.fft.fftshift(X)
    
    Y = H * X
    Y = np.fft.ifftshift(Y)
    y = np.real(np.fft.ifft2(Y))
    
    return y

# Esempio di utilizzo (supponendo che x sia un'immagine caricata):
# x = ml.leggiJPG("lena.jpg")
# y_filtered = gaussLPF(x, sigma=0.1)
# ml.showImage(y_filtered, "lena filtrata")


x = ml.leggiJPG("volto.tif")
y = gaussLPF(x,0.1)
plt.imshow(y, clim=[0,255], cmap="gray")