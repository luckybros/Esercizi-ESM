#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Esercizio 1.1.2

Lo spazio HSI. La rappresentazione HSV si ottiene con skimage.color.rgb2hsv. Il modello 
HSV è leggermente diverso da quello HSI, dato che il solido di riferimento è una piramide 
rovesciata, con la cima nell’origine a differenza del caso HSI in cui il modello è
una doppia piramide. Per questo motivo per il passaggio nello spazio HSI usate le 
funzioni disponibili sul sito del corso nella sezione materiale didattico.
Visualizzate le componenti HSI dell’immagine fragole.jpg e quelle dell’immagine cubo.jpg
che rappre- senta proprio il cubo dei colori. In quest’ultimo caso si possono fare 
alcune interessanti considerazioni. Nell’immagine di tinta, si pu`o notare la forte 
discontinuit`a lungo la linea a 45o sul piano frontale del cubo, che `e quello del 
rosso: si ha infatti lungo questa linea la transizione brusca tra valori alti (360o)
e valori bassi (0o) della tinta, dovuta alla sua rappresentazione circolare. L’immagine
di saturazione mostra valori piu` scuri verso il vertice del bianco, dove i colori 
diventano progressivamente meno saturi. Infine, nell’immagine di intensità, ogni pixel 
e semplicemente la media dei valori RGB del pixel corrispondente nell’immagine a colori.
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
import skimage.color as col
import scipy.ndimage as ndi


f = ml.leggiJPG("fragole.jpg")
c = ml.leggiJPG("cubo.jpg")

f_h = col.rgb2hsv(f)
c_h = col.rgb2hsv(c)
