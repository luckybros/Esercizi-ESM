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
    x = np.float32(io.imread(nomefile))
    #plt.figure()
    #plt.imshow(x, clim = None, cmap = "gray")   
    return x
    
def leggiRAW(nomefile,nRighe,nColonne,tipo):
    x = np.fromfile(nomefile, tipo)
    x = np.reshape(x, (nRighe, nColonne))
    #plt.figure()
    #plt.imshow(x, clim = None, cmap = "gray") 
    return x

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
    
#def loc_equaliz(x):