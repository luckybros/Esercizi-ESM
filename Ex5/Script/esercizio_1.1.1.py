#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Esercizio 1.1.1

Provate a scrivere una funzione con il seguente prototipo: rgb2cmy(x), che legge un’immagine a
colori e determina la rappresentazione CMY dell’immagine fragole.jpg visualizzandone le componenti.
Scrivete poi una funzione dal prototipo: rgb2cmyk(x) che legge un’immagine a colori e determina la 
rappresentazione CMYK (Cyan, Magenta, Yellow, Black) di un’immagine visualizzandone le componenti. 
Tenete presente che quando si usano i pigmenti, il nero si ottiene usando uguali 
quantit`a dei pigmenti ciano, magenta e giallo, e quindi la componente K `e pari 
al minimo fra C, M ed Y, e le nuove componenti dei pigmenti si ottengono sottraendo 
K, cio`e C’=C-K, e così via.
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


x = ml.leggiJPG("fragole.jpg")
x = x/255
z = ml.rgb2cmy(x)
ml.showTwoImages(x, z, "RGB", "CMY")

k = ml.rgb2cmyk(x)
ml.showTwoImages(x, k, "RGB", "CMYK")



    
    
    
    
