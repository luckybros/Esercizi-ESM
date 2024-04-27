#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filtri di smoothing
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
import scipy.ndimage as ndi

x = np.float64(io.imread("test.jpg"))
k = 27   # dimensione della maschera
h = np.ones((k,k))/(k**2)
y = ndi.correlate(x, h, mode="reflect")

ml.showTwoImages(x, y, "Originale", "Blurred")