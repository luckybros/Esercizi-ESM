#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pattern di Moir ́e. L’immagine car.tif `e caratterizzata dal pattern di moir ́e, un artefatto 
piuttosto fasti- dioso che pu`o essere generato da una scansione non appropriata di una fotografia 
stampata su di un giornale. Dopo aver osservato attentamente la trasformata di Fourier dell’immagine, 
scrivete il codice per rimuovere questo disturbo attraverso un opportuno filtro ideale e mostrate 
l’immagine risultante.
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

x = ml.leggiJPG("car.tif")
ml.showImage(x, "car")

X = np.fft.fft2(x)
X = np.fft.fftshift(X)
plt.figure()
plt.imshow(np.log(1+np.abs(X)), clim=None, cmap="gray", extent=(-0.5,+0.5,+0.5,-0.5));
plt.title("Trasformata di Fourier immagine rumorosa"); 

# Definizione del filtro
m = np.fft.fftshift(np.fft.fftfreq(X.shape[0]))
n = np.fft.fftshift(np.fft.fftfreq(X.shape[1]))
l, k = np.meshgrid(n, m)

# Definizione del filtro
mu_1 = 0.15
nu_1 = 0.18
B_1 = 0.023
mu_2 = 0.17
nu_2 = -0.16
B_2 = 0.023
mu_3 = 0.32
nu_3 = 0.18
B_3 = 0.015
mu_4 = 0.34
nu_4 = -0.16
B_4 = 0.015

m = np.fft.fftshift(np.fft.fftfreq(X.shape[0]))
n = np.fft.fftshift(np.fft.fftfreq(X.shape[1]))
l, k = np.meshgrid(n, m)

H_1a = np.sqrt((k - mu_1)**2 + (l - nu_1)**2) <= B_1
H_1b = np.sqrt((k + mu_1)**2 + (l + nu_1)**2) <= B_1
H_2a = np.sqrt((k - mu_2)**2 + (l - nu_2)**2) <= B_2
H_2b = np.sqrt((k + mu_2)**2 + (l + nu_2)**2) <= B_2
H_3a = np.sqrt((k - mu_3)**2 + (l - nu_3)**2) <= B_3
H_3b = np.sqrt((k + mu_3)**2 + (l + nu_3)**2) <= B_3
H_4a = np.sqrt((k - mu_4)**2 + (l - nu_4)**2) <= B_4
H_4b = np.sqrt((k + mu_4)**2 + (l + nu_4)**2) <= B_4

H = ~(H_1a | H_1b | H_2a | H_2b | H_3a | H_3b | H_4a | H_4b)
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
