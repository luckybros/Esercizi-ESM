#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 17:28:44 2024

@author: luketto
"""

import numpy as np              # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi     # importa Scipy per le immagini
import skimage.io as io         # importa il modulo Input/Output di SK-Imagex
import skimage.exposure as ex

def leggiJPG(nomefile): 
    x = np.float64(io.imread(nomefile))
    #plt.figure()
    #plt.imshow(x, clim = None, cmap = "gray")   
    return x
    
def leggiRAW(nomefile,nRighe,nColonne,tipo):
    x = np.fromfile(nomefile, tipo)
    x = np.reshape(x, (nRighe, nColonne))
    #plt.figure()
    #plt.imshow(x, clim = None, cmap = "gray") 
    return x

def showImage(immagine, descrizione):
    plt.figure()
    plt.imshow(immagine, clim=None, cmap="gray")
    plt.title(descrizione)
    
def showTwoImages(nomeImmagine1, nomeImmagine2, descrizione1, descrizione2):
    plt.figure()
    plt.subplot(1,2,1) 
    plt.imshow(nomeImmagine1, clim=None, cmap="gray")
    plt.title(descrizione1)
    plt.subplot(1,2,2) 
    plt.imshow(nomeImmagine2, clim=None, cmap="gray");
    plt.title(descrizione2)
    
def glob_equaliz(x): 
    y = ex.equalize_hist(x)
    y = 255*y
    return y

def smooth(x):
    h = [[1, 2, 1],
         [2, 4, 2],
         [1, 2, 1]]
    for i in range(len(h)):
        for j in range(len(h[i])):
            h[i][j] /= 16
    y = ndi.correlate(x, h, mode="reflect")
    return y
    
def smooth_media_aritmetica(x, k):
    h = np.ones((k,k))/(k**2)
    y = ndi.correlate(x, h, mode="reflect")
    return y

def thresholding(x, soglia):
    max = np.max(x)
    mask = x < (soglia/100)*max
    x[mask] = 0 
    return x

#def loc_equaliz(x):