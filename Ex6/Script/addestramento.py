#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 01:21:54 2024

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
from skimage.feature import hog

#   vettore di etichette (label) per 896 immagini di tessuti tumorali. 
#   L’etichetta `e 1 se l’immagine `e relativa ad un tumore maligno ed `e 0 
#   se l’immagine `e relativa ad un tumore benigno
train_label = np.load("train_label.npy") 

#   La variabile train feat `e una matrice 896 × 256 contenente i vettori di 
#   feature (LBP con intorno circolare, P=8 e R=1) per 896 immagini, uno per 
#   ogni riga.
train_feat = np.load("train_lbp_8_1_default.npy")

# standardizzazione
mu = np.mean(train_feat, 0)
sigma = np.std(train_feat, 0)
train_feat = (train_feat - mu)/(sigma + 1e-15)

from sklearn.svm import LinearSVC
classifier = LinearSVC().fit(train_feat, train_label) # training-phase

# proviamo a classificare questa nuova immagine
x = ml.leggiJPG("test_breakhis.png")
P = 8; R = 1; model = "uniform"

# calcoliamo le features
feat = ml.extract_feature(x, P, R, model)

# normalizziamo
feat = (feat - mu)/(sigma + 1e-15)
feat = np.reshape(feat, (1, -1))

predizione = classifier.predict(feat)
if predizione==1:
   print("tumore maligno")
else:
   print("tumore benigno")
