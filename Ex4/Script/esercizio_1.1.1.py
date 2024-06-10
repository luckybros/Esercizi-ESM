#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Esercizio 1.1.1
Spettro di ampiezza. Analizzate lo spettro di ampiezza di alcune immagini di test 
(circuito.jpg, impron- ta.tif, anelli.tif), siete in grado di legare il contenuto in 
frequenza con l’andamento spaziale dell’immagine?
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

circ = ml.leggiJPG("circuito.jpg")
CIRC = ml.fourier_transform(circ)
ml.showTwoImages(circ, CIRC, "normale", "trasformata")
#ml.graph(CIRC)

anelli = ml.leggiJPG("anelli.tif")
ANELLI = ml.fourier_transform(anelli)
ml.showTwoImages(anelli, ANELLI, "normale", "trasformata")
#ml.graph(ANELLI)

impronta = ml.leggiJPG("impronta.jpg")
IMPRONTA = ml.fourier_transform(impronta)
ml.showTwoImages(impronta, IMPRONTA, "normale", "trasformata")
#ml.graph(IMPRONTA)
