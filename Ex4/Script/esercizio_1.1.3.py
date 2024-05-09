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

k = 15
h = np.ones((k,k))/(k^2)

#N,M = h.shape
#P = 5*N; Q = 5*M

H = np.fft.fft2(h)
H = np.abs(np.fft.fftshift(H))
H = np.log(1+H)

ml.graph(H)