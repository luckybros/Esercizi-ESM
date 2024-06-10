#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Risposta in frequenza del filtro media aritmetica. Calcolate la DFT del filtro media 
aritmetica di di- mensione k = 5, 10, 15, utilizzando per la FFT un numero di punti 
relativamente elevato, allo scopo di ottenere un campionamento fine di H(ν,μ). 
Verificate il comportamento passa-basso del filtro.
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

P = 500; Q = 500;
list_k = [5, 10, 15]
list_H = []

for k in list_k:
    h = np.ones((k,k))/(k^2)
    H = np.fft.fft2(h, (P,Q))
    H = np.fft.fftshift(H)
    H = np.abs(H)
    H = np.log(1 + H)
    
    plt.figure();
    plt.imshow(H, clim=None, cmap="gray", extent=(-0.5,+0.5,+0.5,-0.5));
    plt.title("Risposta in frequenza del filtro media aritmetica per k=%d" % k)
