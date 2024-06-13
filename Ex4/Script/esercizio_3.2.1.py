#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filtraggio notch. L’immagine anelli.tif mostra una parte degli anelli che circondano Saturno. Il 
rumore sinusoidale `e dovuto ad un segnale AC sovrapposto a quello della fotocamera prima di 
digitalizzare l’im- magine. Tale interferenza `e semplice da rimuovere se si progetta un filtro notch 
in grado di cancellare il contributo del rumore. Calcolate quindi la trasformata di Fourier 
dell’immagine, analizzatela, individuate il contributo realtivo al segnale sinusoidale e cercate di 
eliminarlo con il filtraggio.
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

x = ml.leggiJPG("anelli.tif")
ml.showImage(x, "anelli")

X = np.fft.fft2(x)
X = np.fft.fftshift(X)
plt.figure()
plt.imshow(np.log(1+np.abs(X)), clim=None, cmap="gray", extent=(-0.5,+0.5,+0.5,-0.5));
plt.title("Trasformata di Fourier immagine rumorosa");  

# Definizione del filtro
nu = 0.2
B = 0.03

m = np.fft.fftshift(np.fft.fftfreq(X.shape[0]))
n = np.fft.fftshift(np.fft.fftfreq(X.shape[1]))
l, k = np.meshgrid(n, m)

"""
D = np.sqrt(k**2+l**2)
D0 = 0.2
D1 = 0.16
H = ((D>=D0) ^ (D<=D1))
plt.figure();
plt.imshow(H, clim=[0,1], cmap="gray", extent=(-0.5,+0.5,+0.5,-0.5));   # filtro tra 0 ed 1 di colori, in grigio
plt.title("Filtro elimina")
"""
"""
Bk = 0.004
Bl = 0.02
H1 = (-Bk <= k) & (k <= Bk)
H2 = (-Bl <= l) & (l <= Bl)
H = (~H1) | (H2 & H1)
"""
# Definizione delle frequenze da eliminare
Bk = 0.004; Bl = 0.02

H1 = (-Bk <= l) & (l <= Bk)     # striscia grande sulle righe
H2 = (-Bl <= k) & (k <= Bl)     # striscia piccola sulle colonne
H = (~H1) | (H2 & H1)           # striscia piccola in verticale con buco

# ottengo una maschera che taglia l'asse immaginario (il rumore è orizzontale)

plt.figure()
plt.imshow(H, clim=[0,1], cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5))
plt.title('Riposta in frequenza del filtro')

Y = H*X
plt.figure()
plt.imshow(np.log(1 + np.abs(Y)), clim=None, cmap = "gray", extent=(-0.5,+0.5,+0.5,-0.5));
plt.title("Trasformata dell'uscita")

Y = np.fft.ifftshift(Y)
y = np.real(np.fft.ifft2(Y))
plt.figure()
plt.imshow(y, clim=[0,255], cmap="gray")
plt.title("Uscita")
