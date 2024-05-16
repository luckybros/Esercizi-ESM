#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 23:48:02 2024

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
import skimage.data as data
import scipy.ndimage as ndi
from skimage.feature import local_binary_pattern

P = 8; R = 1; model = "uniform"

def extract_feature(x):
    y = local_binary_pattern(x, P, R, model)
    n, b = np.histogram(y, np.arange(np.max(y)+2))
    return n
    
x = np.float64(data.brick())

h0 = np.array([[1,0,0],[0,-1,0],[0,0,0]], dtype=np.float64)
h1 = np.array([[0,1,0],[0,-1,0],[0,0,0]], dtype=np.float64)
h2 = np.array([[0,0,1],[0,-1,0],[0,0,0]], dtype=np.float64)
h3 = np.array([[0,0,0],[0,-1,1],[0,0,0]], dtype=np.float64)
h4 = np.array([[0,0,0],[0,-1,0],[0,0,1]], dtype=np.float64)
h5 = np.array([[0,0,0],[0,-1,0],[0,1,0]], dtype=np.float64)
h6 = np.array([[0,0,0],[0,-1,0],[1,0,0]], dtype=np.float64)
h7 = np.array([[0,0,0],[1,-1,0],[0,0,0]], dtype=np.float64)

h = np.array([h0, h1, h2, h3, h4, h5, h6, h7])

b = []
y = 0

for i in range(h.shape[0]):
    b.append(ndi.correlate(x, h[i]) >= 0)
    y += b[i]*(2**i)
    
ml.showTwoImages(x, y, "originale", "LBP")

# le patch uniformi sono quelle con tutti 1 o 0, cioè di valore in stringa di bit sono
# quelle con 255 e 0
mappa_uniformi = (y == 0) | (y == 255)

ml.showTwoImages(x, mappa_uniformi, "Originale", "Mappa zone uniformi")

# Facciamo adesso un esperimento e usiamo LBP per discriminare differenti 
# tessiture e confrontiamo gli isto- grammi. Possiamo determinate il tipo di 
# tessiture (mattoni, erba o ghiaia) delle immagini img1.jpg, img2.jpg e 
# img3.jpg in base alle distanze SAD (somma delle differenze assolute) degli 
# istogrammi ottenuti dall’immagine dei descrittori locali LBP rispetto agli 
# istogrammi delle immagini brick.png, grass.png e gravel.png.

brick = ml.leggiJPG("brick.png")
grass = ml.leggiJPG("grass.png")
gravel = ml.leggiJPG("gravel.png")

feat_brick = ml.extract_feature(brick)
feat_grass = ml.extract_feature(grass)
feat_gravel = ml.extract_feature(gravel)

confronto = ml.leggiJPG("img3.jpg")
feat_confronto = ml.extract_feature(confronto)

diff_brick = np.sum(np.abs(feat_brick - feat_confronto))
diff_grass = np.sum(np.abs(feat_grass - feat_confronto))
diff_gravel = np.sum(np.abs(feat_gravel - feat_confronto))

min_value = min(diff_brick, diff_grass, diff_gravel)

if min_value == diff_brick:
    print("È un mattone")
elif min_value == diff_grass:
    print("È dell'erba")
else:
    print("È della ghiaia")