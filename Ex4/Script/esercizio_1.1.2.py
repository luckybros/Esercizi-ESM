#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Esercizio 1.1.2
Spettro di fase. Per comprendere l’importanza dello spettro di fase provate a realizzare
il seguente esperimento. Considerate l’immagine volto.tif e dopo averne calcolato e 
visualizzato spettro di ampiezza e di fase, ricostruite l’immagine con la sola 
informazione di ampiezza e poi solo con quella di fase e confrontate le due immagini.
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
VOL = np.fft.fft2(vol)

VOL_M = np.log(1+np.abs((np.fft.fftshift(VOL))))
VOL_P = np.angle((np.fft.fftshift(VOL)))

ml.showTwoImages(VOL_M, VOL_P, "MODULO", "FASE")

ret = ml.leggiJPG("rettangolo.jpg")
RET = np.fft.fft2(vol)

RET_M = np.log(1+np.abs((np.fft.fftshift(RET))))
RET_P = np.angle((np.fft.fftshift(RET)))

vol_mod = np.real(np.fft.ifft2(np.abs(VOL)))
vol_phase = np.real(np.fft.ifft2(np.angle(VOL)))

rett_mod = np.real(np.fft.ifft2(np.abs(RET)))
rett_phase = np.real(np.fft.ifft2(np.exp(1j*np.angle(RET))))

VOL_RIC_1 = vol_mod*np.exp(1j*rett_phase) 
VOL_RIC_2 = rett_mod*np.exp(1j*vol_phase) 

vol_ric_1 = np.fft.ifft2(VOL_RIC_1)
vol_ric_2 = np.fft.ifft2(VOL_RIC_2)

ml.showImage(vol_ric_1, "prima ricostruzione")
ml.showImage(vol_ric_2, "seconda ricostruzione")

