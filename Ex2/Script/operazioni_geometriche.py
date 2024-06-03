#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Operazioni geometriche
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
from skimage.transform import rescale

x = io.imread("marte.jpg")

y = x[::100, ::100] # rimpicciolimento

ml.showTwoImages(x, y, "Normale", "Rimpicciolita")

# se lo si vuole fare con un fattore non intero occorre interpolare
y = rescale(x, 2/3, order=1)
ml.showImage(y, "interpolazione")
# realizziamo una traslazione m' = m + 100 ed n' = n + 50
A = np.array([ [1,0,100], [0,1,50], [0,0,1]], dtype=np.float32)

