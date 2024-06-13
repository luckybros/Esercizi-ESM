#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:27:59 2024

@author: luketto
"""
import sys
sys.path.append('/Users/luketto/Desktop/II Semestre IV Anno/ESM/Esercizi/Librerie')
import MyLibrary as ml
import numpy as np 
import matplotlib.pyplot as plt
import scipy.ndimage as ndi 
import skimage.io as io

k = 25

x = np.float64(io.imread('lenac.jpg'))/255

y = ndi.uniform_filter(x, (k,k,1))
#equivalente a  y = ndi.uniform_filter(x, (k,k,1))

ml.showTwoImages(x, y, "normale", "media (RBG)")

x_hsi = ml.rgb_to_hsi(x)
x_hsi[:,:,2] = ndi.uniform_filter(x_hsi[:,:,2], (k,k))

y = ml.hsi_to_rgb(x_hsi)

ml.showTwoImages(x, y, "normale", "media (HSI)")