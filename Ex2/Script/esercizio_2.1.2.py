#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Esercizio 2.1.2
Esempio di Watermarking. Provate adesso a realizzare una forma molto semplice di 
watermarking, che consiste nell’inserire una firma digitale all’interno di un’immagine. 
Sostituite il bit-plane meno significativo dell’immagine lena.y con l’immagine binaria 
marchio.y. Quest’ultima ha dimensioni 350×350 quindi `e necessario estrarre una sezione 
delle stesse dimensioni dell’immagine lena.y. Provate poi a ricostruire l’immagine e 
visualizzatela, noterete che da un punto di vista visivo l’immagine non ha subito 
modifiche percettibili.
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

lena = ml.leggiRAW("lena.y", 512, 512, np.uint8)
marchio = ml.leggiRAW("marchio.y", 350, 350, np.uint8)

padding_superiore_sinistra = (0, 162)  # Numero di righe da aggiungere sopra e numero di colonne da aggiungere a sinistra
padding_inferiore_destra = (162, 0)    # Numero di righe da aggiungere sotto e numero di colonne da aggiungere a destra

marchio_espanso = np.pad(marchio, (padding_superiore_sinistra, padding_inferiore_destra), mode="constant")

lena_marchio = bit.bitset(lena, 7, marchio_espanso)

plt.figure()
plt.subplot(1,2,1) 
plt.imshow(lena, clim=None, cmap="gray")
plt.title('Lena Originale')
plt.subplot(1,2,2) 
plt.imshow(lena_marchio, clim=None, cmap="gray");
plt.title('Lena con marchio')
