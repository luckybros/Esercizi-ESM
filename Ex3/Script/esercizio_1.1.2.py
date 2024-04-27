#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Esercizio 1.1.2
Smoothing seguito da thresholding. Un’importante applicazione dei filtri che realizzano 
la media spaziale è quello di sfocare l’immagine in modo da confondere con lo sfondo 
oggetti piccoli di poco interesse ed enfatizzare oggetti più grandi, che quindi 
possono essere facilmente rilevati. Consideriamo, ad esempio, l’immagine spazio.jpg, 
proveniente dal telescopio Hubble, in orbita intorno alla terra. Realizzate le seguenti 
operazioni:
(a) visualizzate l’immagine;
(b) applicate il filtro che effettua la media aritmetica su una finestra di dimensioni 
15×15 e visualizzate il risultato;
(c) realizzate un’operazione a soglia (thresholding) per eliminare oggetti piccoli, 
in particolare consi- derate una soglia pari al 25 per cento del valore massimo 
presente nell’immagine filtrata;
(d) visualizzate il risultato dell’elaborazione.
Noterete che la scelta della dimensione della maschera deve essere confrontabile 
con gli oggetti che si vogliono trascurare, provate a modificarne la dimensione e 
valutatene gli effetti, variando anche la soglia opportunamente.
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

x = ml.leggiJPG("space.jpg")
y = ml.smooth_media_aritmetica(x, 15)
ml.showTwoImages(x, y, "Originale", "Blurred")
z = ml.thresholding(y, 25)    #   si annullano tutti i valori minori della soglia 

w = x * z

ml.showImage(z, "Thresholding")
