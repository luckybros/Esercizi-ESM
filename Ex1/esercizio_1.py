#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Esercizio 1
Lettura e visualizzazione di un’immagine. Provate a scrivere una funzione in grado di visualizzare le im- 
magini sia in formato JPEG che in formato grezzo. Il prototipo delle funzioni deve essere 
rispettivamente: vediJPG(nomefile) e vediRAW(nomefile,nRighe,nColonne,tipo)
"""

import numpy as np              # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi     # importa Scipy per le immagini
import skimage.io as io         # importa il modulo Input/Output di SK-Image

def vediJPG(nomefile): 
    x = io.imread(nomefile)
    plt.figure()
    plt.imshow(x, clim = None, cmap = "gray")   
    
def vediRAW(nomefile,nRighe,nColonne,tipo):
    x = np.fromfile(nomefile, tipo)
    x = np.reshape(x, (nRighe, nColonne))
    plt.figure()
    plt.imshow(x, clim = None, cmap = "gray") 
    
vediJPG("dorian.jpg")
vediRAW("house.y", 512, 512, np.uint8)

