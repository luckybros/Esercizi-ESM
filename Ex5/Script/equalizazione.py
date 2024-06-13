#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Equalizzazione
"""
import sys
sys.path.append('/Users/luketto/Desktop/II Semestre IV Anno/ESM/Esercizi/Librerie')
import MyLibrary as ml
import numpy as np 
import matplotlib.pyplot as plt
import scipy.ndimage as ndi 
import skimage.io as io
from skimage.exposure import equalize_hist
#from color_conversion import rgb2hsi, hsi2rgb

#equalizzazione dell'istogramma -> appiattimento.

x = np.float64(io.imread('volto.tiff'))/255

#rgb.

r = x[:,:,0]
g = x[:,:,1]
b = x[:,:,2]

r = equalize_hist(r)
g = equalize_hist(g)
b = equalize_hist(b)

y = np.stack((r,g,b), -1)

#hsi.
x_hsi = ml.rgb_to_hsi(x)
h = x_hsi[:,:,0]
s = x_hsi[:,:,1]
i = x_hsi[:,:,2]

i = equalize_hist(i)

y_hsi = np.stack((h,s,i), -1)
Y = ml.hsi_to_rgb(y_hsi)
#z = rgb2hsi(x)
#z[:,:,2] = equalize_hist(z[:,:,2])
#z = hsi2rgb(z)

ml.showTwoImages(x, y, "normale", "equalizzazione RGB")
ml.showTwoImages(x, Y, "normale", "equalizzazione HSI (solo I)")
#plt.subplot(1,3,3); plt.imshow(z);