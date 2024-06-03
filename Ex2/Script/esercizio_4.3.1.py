#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Esercizio 4.3.1
Distorsione. Scrivete la funzione che realizza la distorsione di un’immagine 
lungo la direzione verticale e orizzontale e che abbia il prototipo: 
deforma(x,c,d). Scegliete un’immagine e al variare dei parametri c e d 
osservate il tipo di distorsione.
"""

import sys
sys.path.append('/Users/luketto/Desktop/II Semestre IV Anno/ESM/Esercizi/Librerie')
import MyLibrary as ml
import numpy as np              # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi     # importa Scipy per le immagini
import skimage.io as io         # importa il modulo Input/Output di SK-Imagex
import skimage.exposure as ex
from skimage.transform import warp

def deforma(x, c, d):
    A = np.array([ [1,d,0], [c,1,0], [0,0,1]], dtype=np.float32)
    y = warp(x, A, order=1, cval=0)   # colore bianco
    return y 

x = np.float32(io.imread("lena.jpg"))
y = deforma(x, 0.5, 0.5)

ml.showTwoImages(x, y, "normale", "distorta")
