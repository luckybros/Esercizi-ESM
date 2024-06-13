#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 18:46:48 2024

@author: luketto
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

x = np.fromfile("lenarumorosa_verticale.y", np.int16)
x = np.reshape(x, [512,512])
x = np.float64(x)
ml.showImage(x, "immagine rumorosa")

X = np.fft.fft2(x)
X = np.fft.fftshift(X)
plt.figure()
plt.imshow(np.log(1+np.abs(X)), clim=None, cmap="gray", extent=(-0.5,+0.5,+0.5,-0.5));
plt.title("Trasformata di Fourier immagine rumorosa");  

"""
Poiché il rumore sinusoidale è finestrato, in frequenza dovrebbe essere pari a due impulsi
ma il prodotto tra il seno e la finestra corrisponde alla convoluzione tra i due impulsi
e una sinc bidimensionale, che corrisponde proprio a due sinc centrate nella frequenza della sinusoide
"""

#ml.graph(np.abs(np.log(1+np.abs((np.fft.fftshift(X))))))
"""
# Definizione del filtro
nu = 0.2
B = 0.03

m = np.fft.fftshift(np.fft.fftfreq(X.shape[0]))
n = np.fft.fftshift(np.fft.fftfreq(X.shape[1]))
l, k = np.meshgrid(n, m)
D1 = np.sqrt(k**2 + (l - nu)**2)
D2 = np.sqrt(k**2 + (l + nu)**2)
H = (D1 > B) & (D2 > B)

plt.figure()
plt.imshow(H, clim=[0,1], cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5))
plt.title('Riposta in frequenza del filtro')

# Filtraggio
Y = X * H
plt.figure()
plt.imshow(np.log(1+np.abs(Y)), clim=None, cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5))
plt.title('Trasformata di Fourier immagine filtrata')

y = np.real(np.fft.ifft2(np.fft.ifftshift(Y)))
ml.showImage(y, "Immagine filtrata")

xo = ml.leggiJPG("lena.jpg")
xo = np.float64(np.reshape(xo, [512,512]))

MSE = np.mean((xo-y) ** 2)

print(MSE)
"""
# Definizione del filtro
m = np.fft.fftshift(np.fft.fftfreq(X.shape[0]))
n = np.fft.fftshift(np.fft.fftfreq(X.shape[1]))
l, k = np.meshgrid(n, m)

Bk = 0.004
Bl = 0.02
H1 = (-Bk <= k) & (k <= Bk)     # striscia piccola sulle righe
H2 = (-Bl <= l) & (l <= Bl)     # striscia grande sulle colonne
H = (~H1) | (H2 & H1)           # striscia piccola in orizzontale con buco in mezzo
# ottengo una maschera che taglia l'asse reale (il rumore è verticale)
 
"""
plt.figure()
plt.imshow(H1, clim=[0,1], cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5))
plt.title('H1 = (-Bk <= k) & (k <= Bk)')

plt.figure()
plt.imshow(H2, clim=[0,1], cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5))
plt.title('H2 = (-Bl <= l) & (l <= Bl)')

plt.figure()
plt.imshow(~H1, clim=[0,1], cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5))
plt.title('(~H1)')

plt.figure()
plt.imshow((H2 & H1), clim=[0,1], cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5))
plt.title('(H2 & H1)')

"""
plt.figure()
plt.imshow(H, clim=[0,1], cmap='gray', extent=(-0.5,+0.5,+0.5,-0.5))
plt.title('Riposta in frequenza del filtro')


Y = X * H
y = np.real(np.fft.ifft2(np.fft.ifftshift(Y)))

plt.figure()
plt.imshow(y, clim=[0,256], cmap='gray')
plt.title('Immagine filtrata')

xo = ml.leggiJPG("lena.jpg")
xo = np.float64(np.reshape(xo, [512,512]))

MSE = np.mean((xo-y) ** 2)
print(MSE)

# se i rumori sono sinusoidi verticali allora gli impulsi da eliminare saranno sull'asse
# reale, mentre se sono sinusoidi orizzontali allora gli impulsi da eliminare saranno
# sull'asse immaginario

