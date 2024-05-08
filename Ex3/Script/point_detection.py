#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Point & Line detection
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

x = ml.leggiJPG("turbina.jpg")
h = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]], dtype=np.float64)
z = ndi.correlate(x, h)

y = ml.thresholding(z, 90)

ml.showImage(y, "ciao")
