#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filtro medano
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

x = np.float64(io.imread("circuito_rumoroso.jpg"))
y = ndi.median_filter(x, (5,5))

ml.showTwoImages(x, y, "originale", "mediano")

