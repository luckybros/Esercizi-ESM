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

def show_three_images(image1, description1, image2, description2, image3, description3):
    plt.figure(figsize=(12, 4))  # Imposta le dimensioni della figura

    # Prima immagine
    plt.subplot(1, 3, 1)
    plt.imshow(image1, cmap='gray')  # Mostra l'immagine in scala di grigi
    plt.title(description1)  # Imposta il titolo

    # Seconda immagine
    plt.subplot(1, 3, 2)
    plt.imshow(image2, cmap='gray')
    plt.title(description2)

    # Terza immagine
    plt.subplot(1, 3, 3)
    plt.imshow(image3, cmap='gray')
    plt.title(description3)

    plt.show()  # Mostra la figura con tutte e tre le immagini
    
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

def rgb2cmy(x):
    y = 1.0 - x
    return y

def rgb2cmyk(x):
    z = rgb2cmy(x)
    k = np.min(z, 2)
    c = z[:,:,0]
    m = z[:,:,1]
    y = z[:,:,2]
    return np.stack((c,m,y,k),2)

#def loc_equaliz(x):