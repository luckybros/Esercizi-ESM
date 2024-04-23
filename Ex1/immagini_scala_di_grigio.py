#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 00:07:12 2024

@author: luketto
"""

import numpy as np              # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi     # importa Scipy per le immagini
import skimage.io as io         # importa il modulo Input/Output di SK-Image

x = io.imread("dorian.jpg");    # leggiamo il file
(M,N) = x.shape                 # memorizziamo le dimensioni in M e N

y = np.fromfile("house.y", np.uint8) # lettura dei dati da file

# y è un vettore

y = np.reshape(y, (512, 512))

# notiamo come io.imread restituisca direttamente la matrice mentre il comando
# np.fromfile restituisce un vettore a cui bisogna fare reshape

# passiamo ora alla visualizzazione
plt.figure(1)
plt.imshow(x, clim = None, cmap = "gray")    

# clim indica il range di visualizzazione,
# mentre cmap indica che l'immagine verrà visualizzata 
# in scala di grigi
# se si indica None allora il range di rappresentabilitò
# sarà [min(x), max(x)]                                         
                                            
                                            
