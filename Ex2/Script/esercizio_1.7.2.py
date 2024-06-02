#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Esercizio 1.7.2
poich ́e nemmeno questa operazione risolve il problema ricorrete all’enhancement 
locale, effettuate cioè l’equalizzazione dell’istogramma su blocchi 3×3 
dell’immagine e conservate solo il pixel centrale del bloc- co elaborato. 
A tale scopo scrivete la funzione function y = loc equaliz(x), e mostrate 
l’immagine elaborata.
"""
import sys
sys.path.append('/Users/luketto/Desktop/II Semestre IV Anno/ESM/Esercizi/Librerie')
import MyLibrary as ml
import numpy as np              # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi     # importa Scipy per le immagini
import skimage.io as io         # importa il modulo Input/Output di SK-Imagex
import skimage.exposure as ex

    
x = ml.leggiJPG("quadrato.tif")
n, b = np.histogram(x, np.arange(257))  # istogramma
plt.figure()
plt.bar(np.arange(256), n)
plt.axis([0,255,0,1.1*np.max(n)])
plt.title('Istogramma prima')

y = ndi.generic_filter(x, ml.loc_equaliz, (3,3))

ny, by = np.histogram(y, np.arange(257))  # istogramma

plt.figure()
plt.bar(np.arange(256), ny)
plt.axis([0,255,0,1.1*np.max(ny)])
plt.title('Istogramma dopo equalizzazione')

ml.showTwoImages(x, y, "Originale", "Modificata")