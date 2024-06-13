#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Color balancing
"""
import sys
sys.path.append('/Users/luketto/Desktop/II Semestre IV Anno/ESM/Esercizi/Librerie')
import MyLibrary as ml
import numpy as np 
import matplotlib.pyplot as plt
import scipy.ndimage as ndi 
import skimage.io as io
from skimage.exposure import equalize_hist

x = np.float64(io.imread('foto.jpg'))/255

y = 1.0 - x
c = y[:,:,0]

c = c**1.4

y[:,:,0] = c

y = 1.0 - y

ml.showTwoImages(x, y, "originale", "modificata")

