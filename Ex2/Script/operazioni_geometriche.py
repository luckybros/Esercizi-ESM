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

x = io.imread("marte.jpg")

y = x[::2, ::2] # rimpicciolimento

ml.showTwoImages(x, y, "Normale", "Rimpicciolita")

# realizziamo una traslazione m' = m + 100 ed n' = n + 50
A = np.array([ [1,0,100], [0,1,50], [0,0,1]], dtype=np.float32)