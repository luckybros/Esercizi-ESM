#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Esercizio 4
Immagine delle varianze. Scrivete adesso una funzione dal prototipo varianze(x,K) per calcolare l’immagine 
delle varianze locali su finestre K × K. Usate questa funzione per valutare e visualizzare l’immagine delle varianze 
dell’immagine filamento.jpg usando blocchi 3 × 3. Che tipo di informazioni vi d`a sull’immagine?
"""

import numpy as np              # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi     # importa Scipy per le immagini
import skimage.io as io         # importa il modulo Input/Output di SK-Image

def varianze(x, k):
    """
    Data un'immagine x fornisce l'immagine delle varianze locali usando una finestra
    K x K
    """
    y = ndi.generic_filter(x, np.var, (k,k))
    return y

x = io.imread("filamento.jpg")

y = varianze(x, 3)

plt.figure()
plt.imshow(y, clim = None, cmap = "gray")    