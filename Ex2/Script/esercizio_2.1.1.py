#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Esercizio 2.1.1
Ricostruzione mediante bit-plane. Ponete a zero i bit-plane meno significativi di 
un’immagine (usate la funzione bitset del file bitop.py ) e visualizzate il risultato 
al variare del numero di bit-plane che utilizzate nel processo di ricostruzione. 
Questo esperimento vi permette di stabilire fino a che punto (almeno da un punto di 
vista percettivo) sia possibile diminuire il numero di livelli usati nel processo di 
quantizzazione.
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

x = io.imread("frattale.jpg")

for i in range(8):
    x = bit.bitset(x, i, 0)
    plt.figure()
    plt.imshow(x, clim=[0,255], cmap="gray")
    plt.title('Bitplane %d-esimo annullato' % i)

