#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 17:42:08 2024

@author: luketto
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
import skimage.color as col
import scipy.ndimage as ndi

vol = ml.leggiJPG("volto.tif")
ret = ml.leggiJPG("rettangolo.jpg")

VOL = np.fft.fft2(vol)
RET = np.fft.fft2(ret)

VOL_MOD = np.abs(VOL)
VOL_PHASE = np.exp(1j*np.angle(VOL))
RETT_MOD = np.abs(RET)
RETT_PHASE = np.exp(1j*np.angle(RET))

ric_1 = np.real(np.fft.ifft2(VOL_MOD*RETT_PHASE))
ric_2 = np.real(np.fft.ifft2(RETT_MOD*VOL_PHASE))

ml.showTwoImages(ric_1, ric_2, "modulo volto, fase rettangolo", "modulo rettangolo, fase volto")