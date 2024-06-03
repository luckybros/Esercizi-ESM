#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Esercizio 4.3.2
Rotazione Centrale. Scrivete una funzione con il prototipo ruota(x, theta) 
che utilizza la funzione wrap per ruotare di un’angolo theta l’immagine x 
rispetto al centro dell’immagine. A tal fine usarte una combinazione di 
traslazioni e rotazione. Ricordatevi che la combinazione di diverse 
trasformazioni affini `e ancora una trasformazione affine, che pu`o essere 
ottenuta tramite il prodotto (matriciale) delle matrici che le definiscono.
"""

import sys
sys.path.append('/Users/luketto/Desktop/II Semestre IV Anno/ESM/Esercizi/Librerie')
import MyLibrary as ml
import numpy as np              # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi     # importa Scipy per le immagini
import skimage.io as io         # importa il modulo Input/Output di SK-Imagex
import skimage.exposure as ex
from skimage.transform import warp

def ruota(x, theta):
    M,N = x.shape
    A1 = np.array([[1, 0, N/2], 
               [0, 1, M/2],
               [0, 0, 1]], dtype=np.float32)
              
    A2 = np.array([[np.cos(theta), np.sin(theta), 0], 
               [-np.sin(theta), np.cos(theta), 0],
               [0, 0, 1]], dtype=np.float32)

    A3 = np.array([[1, 0, -N/2], 
               [0, 1, -M/2],
               [0, 0, 1]], dtype=np.float32)
    A = A1 @ A2 @ A3
    y = warp(x, A, order=1)
    return y


x = np.float32(io.imread("lena.jpg"))
y = ruota(x, (np.pi/4))
ml.showTwoImages(x, y, "normale", "distorta")
