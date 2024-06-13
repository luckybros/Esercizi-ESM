#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 14:54:00 2024

@author: luketto
"""

import sys
sys.path.append('/Users/luketto/Desktop/II Semestre IV Anno/ESM/Esercizi/Librerie')
import MyLibrary as ml
import numpy as np 
import matplotlib.pyplot as plt
import scipy.ndimage as ndi 
import skimage.io as io

#correzione di toni e colori -> potenza per migliorare il contrasto.

x = np.float64(io.imread('montagna.jpg'))/255

y = x**0.5

ml.showTwoImages(x, y, "originale", "contrasto aumentato")