#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Line detection
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

x = ml.leggiJPG("quadrato.tif")

h0 = np.array([[-1,-1,-1],
                        [2,2,2],
                        [-1,-1,-1]], dtype=np.float64)
h1 = np.array([[-1,-1,2],
                        [-1,2,-1],
                        [2,-1,-1]], dtype=np.float64)
h2 = np.array([ [-1,2,-1],
                        [-1,2,-1],
                        [-1,2,-1]], dtype=np.float64)
h3 = np.array([[2,-1,-1],
                        [-1,2,-1],
                        [-1,-1,2]], dtype=np.float64)

z0 = ndi.correlate(x, h0)
z1 = ndi.correlate(x, h1)
z2 = ndi.correlate(x, h2)
z3 = ndi.correlate(x, h3)

y0 = ml.thresholding(z0, 90)
ml.showImage(y0, "orizzontale")

y1 = ml.thresholding(z1, 90)
ml.showImage(y1, "obliquo destro")

y2 = ml.thresholding(z2, 90)
ml.showImage(y2, "verticale")

y3 = ml.thresholding(z3, 90)
ml.showImage(y3, "obliquo sinistro")