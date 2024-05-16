#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Composizione delle caratteristiche. Provate a cambiare i parametri del 
descrittore LBP utilizzando 12 vicini e raggio 2. I relativi dati di training 
sono memorizzati nel file train lbp 12 2.npy. Inoltre provate ad utilizzare 
insieme le due varianti LBP concatenando i vettori delle feature.
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
from skimage.feature import hog

#   vettore di etichette (label) per 896 immagini di tessuti tumorali. 
#   L’etichetta `e 1 se l’immagine `e relativa ad un tumore maligno ed `e 0 
#   se l’immagine `e relativa ad un tumore benigno
train_label = np.load("train_label.npy") 

#   La variabile train feat `e una matrice 896 × 256 contenente i vettori di 
#   feature (LBP con intorno circolare, P=8 e R=1) per 896 immagini, uno per 
#   ogni riga.
train_feat_8_1 = np.load("train_lbp_8_1_default.npy")
train_feat_12_2 = np.load("train_lbp_12_2_default.npy")

# standardizzazione 1
mu_8_1 = np.mean(train_feat_8_1, 0)
sigma_8_1 = np.std(train_feat_8_1, 0)
train_feat_8_1 = (train_feat_8_1 - mu_8_1)/(sigma_8_1 + 1e-15)

# standardizzazione 2
mu_12_2 = np.mean(train_feat_12_2,  0)
sigma_12_2 = np.std(train_feat_12_2 , 0)
train_feat_12_2  = (train_feat_12_2  - mu_12_2)/(sigma_12_2 + 1e-15)

from sklearn.svm import LinearSVC
classifier_8_1 = LinearSVC().fit(train_feat_8_1, train_label) # training-phase
classifier_12_2 = LinearSVC().fit(train_feat_12_2, train_label) # training-phase

# proviamo a classificare questa nuova immagine
x = ml.leggiJPG("test_breakhis.png")
P = 8; R = 1; model = "uniform"

# calcoliamo le features
feat = ml.extract_feature(x, P, R, model)

# normalizziamo
feat_8_1 = (feat - mu_8_1)/(sigma_8_1 + 1e-15)
feat_8_1 = np.reshape(feat, (1, -1))
feat_12_2 = (feat - mu_12_2)/(sigma_12_2 + 1e-15)
feat_12_2 = np.reshape(feat, (1, -1))

predizione_8_1 = classifier_8_1.predict(feat_8_1)
predizione_12_2 = classifier_12_2.predict(feat_12_2)

if predizione_8_1==1:
   print("tumore maligno (8-1)")
else:
   print("tumore benigno (8-1)")
   
if predizione_12_2==1:
   print("tumore maligno (12-2)")
else:
   print("tumore benigno (12-2)")   