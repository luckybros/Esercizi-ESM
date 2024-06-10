#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Esercizio 2.1.5
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
import scipy.ndimage as ndi

NORM = 255

def filtro_guidato(x, g, B, epsilon):
    # Normalizzazione
    x = x/NORM
    g = g/NORM
    
    # Calcolo delle medie
    med_x = ndi.generic_filter(x, np.mean, (B,B))
    med_g = ndi.generic_filter(g, np.mean, (B,B))
    
    # Calcolo delle varianze
    var_g = ndi.generic_filter(g, np.var, (B,B))
    
    # Correlazione
    corr_gx = ndi.generic_filter(x*g, np.mean, (B,B))
    
    # Uscita del filtro
    a = (corr_gx - med_x*med_g) / (var_g + epsilon)
    b = med_x - a*med_g
    
    mu_a = ndi.generic_filter(a, np.mean, (B,B))
    mu_b = ndi.generic_filter(b, np.mean, (B,B))
    
    y = mu_a*g + mu_b
    
    return y
    
image = ml.leggiJPG("guida.png")
mask = ml.leggiJPG("mask.png")

y = filtro_guidato(image, mask, 10, 2**-60)

ml.showTwoImages(image, y, "cacca", "culo")