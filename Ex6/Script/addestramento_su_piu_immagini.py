#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 02:00:28 2024

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
import sklearn.metrics as met
import scipy.ndimage as ndi
from skimage.feature import hog

R = 1; P = 8; method = "default"; # settings for LBP

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

list_feats = list() # lista delle feature da riempire
list_label = list() # lista delle etichette da riempire

from glob import glob  # Funzione utile per ottenere una lista di file

# Estrazione feature per immagini con tumore maligno
list_files_malignant = glob('testset/malignant/*.png')
for filename in list_files_malignant:
    # Calcolo feature per un’immagine
    ft = ml.extract_feature(col.rgb2gray(ml.leggiJPG(filename)), P, R, method)
    list_feats.append(ft)  # Inserimento feature nella lista
    list_label.append(1)   # Inserimento etichetta nella lista

# Estrazione feature per immagini con tumore benigno
list_files_benign = glob('testset/benign/*.png')
for filename in list_files_benign:
    ft = ml.extract_feature(col.rgb2gray(ml.leggiJPG(filename)), P, R, method)
    list_feats.append(ft)
    list_label.append(0)


feats = np.stack(list_feats, 0)  # Conversione lista in array
y_true = np.stack(list_label)     # Conversione lista in array
feats = (feats - mu) / (sigma + 1e-15)  # Normalizzazione

y_pred = classifier.predict(feats)  # Classificazione

# Calcolo dell’accuratezza
acc = met.accuracy_score(y_true, y_pred)
print(met.confusion_matrix(y_true, y_pred))