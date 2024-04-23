#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Esercizio 2
Rappresentazione in falsi colori. La rappresentazione in pseudocolori (o falsi colori) consiste nel vi- 
sualizzare a colori un’immagine monocromatica. L’obiettivo è quello di migliorare l’interpretazione di 
un’immagine su livelli di grigio o semplicemente visualizzarla piu` facilmente. Infatti, l’occhio umano è
in grado di discriminare migliaia di variazioni di colore rispetto a qualche decina di livelli di grigio.
Un esempio di rappresentazione in falsi colori riguarda le immagini multispettrali. Queste sono un insieme di 
immagini, ognuna delle quali è stata rilevata dal satellite in una diversa banda spettrale. Considerate le 4 
immagini telerilevate di Washington, in cui è presente una regione con il fiume Potomac. Le prime tre immagini 
sono state rilevate nelle tre bande del visibile, mentre la quarta è nel vicino infrarosso. Provate a visualizzare 
le prime tre immagini come immagine a colori e poi sostituite alla componente R, la quarta immagine, quindi confrontate 
le due figure. Noterete come nella seconda immagine il fiume (vegetazione) è piu` facilmente discriminabile dalla città. 
Infatti il vicino infrarosso è molto sensibile alle parti di una scena contenenti biomasse, e l’immagine 
mostra effettivamente in maniera chiara le differenze tra le componenti naturali (in rosso) e le costruzioni, 
composte principalmemte da asfalto e cemento (tendenti al blu).
"""

import numpy as np              # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi     # importa Scipy per le immagini
import skimage.io as io         # importa il modulo Input/Output di SK-Image

green = io.imread("Washington_green.tif")
red = io.imread("Washington_red.tif")
blue = io.imread("Washingyon_blue.TIF")
infrared = io.imread("Washington_infrared.tif")

colored = np.stack((red, green, blue), -1)
plt.figure()
plt.imshow(colored, clim=None, cmap="gray")
plt.title("A colori")

colored_infrared = np.stack((infrared, green, blue), -1)
plt.figure()
plt.imshow(colored_infrared, clim=None, cmap="gray")
plt.title("A colori con infrarosso")