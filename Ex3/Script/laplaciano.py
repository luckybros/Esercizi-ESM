#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filtri di sharpening
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

x = ml.leggiJPG("luna.jpg")
h = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]], dtype=np.float64)
z = ndi.correlate(x, h)


ml.showTwoImages(x, z, "Originale", "Filtrata")

