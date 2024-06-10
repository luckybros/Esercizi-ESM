#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Esercizio 1.1.2
Spettro di fase. Per comprendere l’importanza dello spettro di fase provate a realizzare
il seguente esperimento. Considerate l’immagine volto.tif e dopo averne calcolato e 
visualizzato spettro di ampiezza e di fase, ricostruite l’immagine con la sola 
informazione di ampiezza e poi solo con quella di fase e confrontate le due immagini.
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

x = np.float64(io.imread("volto.tif"))
X = np.fft.fft2(x)
Xf = np.fft.fftshift(X)
Z = np.log(1 + np.abs(Xf))      # spettro di ampiezza
Z_f = np.angle(Xf)              # spettro di fase

plt.subplot(1,2,1);
plt.imshow(Z,clim=None,cmap="gray", extent=(-0.5,+0.5,+0.5,-0.5));
plt.title("Spettro di ampiezza");
plt.subplot(122);
plt.imshow(np.angle(Xf), clim=[-np.pi, np.pi], cmap="gray", extent=(-0.5,+0.5,+0.5,-0.5));
plt.title("Spettro di fase");

ym = np.real(np.fft.ifft2(np.abs(X)))              # ricostruzione solo modulo
yf = np.real(np.fft.ifft2(np.exp(1j*np.angle(X)))) # ricostruzione solo fase

ml.showTwoImages(ym, yf, "Ricostruzione spettro di ampiezza", "Ricostruzione spettro di fase")

