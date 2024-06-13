#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 17:28:44 2024

@author: luketto
"""

import numpy as np              # importa Numpy
import matplotlib.pyplot as plt # importa Matplotlib
import scipy.ndimage as ndi     # importa Scipy per le immagini
import skimage.io as io         # importa il modulo Input/Output di SK-Imagex
import skimage.exposure as ex
from skimage.feature import local_binary_pattern

def leggiJPG(nomefile): 
    x = np.float64(io.imread(nomefile))
    #plt.figure()
    #plt.imshow(x, clim = None, cmap = "gray")   
    return x
    
def leggiRAW(nomefile,nRighe,nColonne,tipo):
    x = np.fromfile(nomefile, tipo)
    x = np.reshape(x, (nRighe, nColonne))
    #plt.figure()
    #plt.imshow(x, clim = None, cmap = "gray") 
    return x

def showImage(immagine, descrizione):
    plt.figure()
    plt.imshow(immagine, clim=None, cmap="gray")
    plt.title(descrizione)
    
def showTwoImages(nomeImmagine1, nomeImmagine2, descrizione1, descrizione2):
    plt.figure()
    plt.subplot(1,2,1) 
    plt.imshow(nomeImmagine1, clim=None, cmap="gray")
    plt.title(descrizione1)
    plt.subplot(1,2,2) 
    plt.imshow(nomeImmagine2, clim=None, cmap="gray");
    plt.title(descrizione2)

def show_three_images(image1, description1, image2, description2, image3, description3):
    plt.figure(figsize=(12, 4))  # Imposta le dimensioni della figura

    # Prima immagine
    plt.subplot(1, 3, 1)
    plt.imshow(image1, cmap='gray')  # Mostra l'immagine in scala di grigi
    plt.title(description1)  # Imposta il titolo

    # Seconda immagine
    plt.subplot(1, 3, 2)
    plt.imshow(image2, cmap='gray')
    plt.title(description2)

    # Terza immagine
    plt.subplot(1, 3, 3)
    plt.imshow(image3, cmap='gray')
    plt.title(description3)

    plt.show()  # Mostra la figura con tutte e tre le immagini
    
def show_histogram(x):
    n, b = np.histogram(x, np.arange(257))  # istogramma
    plt.figure()
    plt.bar(np.arange(256), n)
    plt.axis([0,255,0,1.1*np.max(n)])
    plt.title('Istogramma di %d' %x)
    
def extract_feature(x, P, R, model):
    y = local_binary_pattern(x, P, R, model)
    n, b = np.histogram(y.flatten(), bins=np.arange(0,257), density=True)
    return n
    
def glob_equaliz(x): 
    y = ex.equalize_hist(x)
    y = 255*y
    return y

def loc_equaliz(b):
    b = np.reshape(b, (3,3))
    b = ex.equalize_hist(b/255)
    y = b[1][1]
    return y

def smooth(x):
    h = [[1, 2, 1],
         [2, 4, 2],
         [1, 2, 1]]
    for i in range(len(h)):
        for j in range(len(h[i])):
            h[i][j] /= 16
    y = ndi.correlate(x, h, mode="reflect")
    return y
    
def smooth_media_aritmetica(x, k):
    h = np.ones((k,k))/(k**2)
    y = ndi.correlate(x, h, mode="reflect")
    return y

def thresholding(x, soglia):
    max = np.max(x)
    mask = x < (soglia/100)*max
    x[mask] = 0 
    return x

def rgb2cmy(x):
    y = 1.0 - x
    return y

def rgb2cmyk(x):
    z = rgb2cmy(x)
    k = np.min(z, 2)
    c = z[:,:,0]
    m = z[:,:,1]
    y = z[:,:,2]
    return np.stack((c,m,y,k),2)

def fourier_transform(x):
    X = np.fft.fft2(x)
    X = np.abs(X)
    X = np.fft.fftshift(X)
    X = np.log(1+X)
    return X

def graph(Y):
    m = np.fft.fftshift(np.fft.fftfreq(Y.shape[0]))
    n = np.fft.fftshift(np.fft.fftfreq(Y.shape[1]))
    ax = plt.figure().add_subplot(projection='3d')
    l,k = np.meshgrid(n,m)
    ax.plot_surface(l,k,Y, linewidth=0, cmap="jet")
    
def gaussLPF(x, sigma):
    M, N = x.shape
    m = np.fft.fftshift(np.fft.fftfreq(M))
    n = np.fft.fftshift(np.fft.fftfreq(N))
    l, k = np.meshgrid(n, m)
    D = np.sqrt(k**2 + l**2)
    
    H = np.exp(-(D**2) / (2 * sigma**2))  # filtro gaussiano
    
    X = np.fft.fft2(x)
    X = np.fft.fftshift(X)
    
    Y = H * X
    Y = np.fft.ifftshift(Y)
    y = np.real(np.fft.ifft2(Y))
    
    return y


def rgb_to_hsi(image):
    # Convert the image to float and normalize
    #image = image.astype(np.float32) / 255.0
    R, G, B = image[:,:,0], image[:,:,1], image[:,:,2]
    
    # Intensity calculation
    I = (R + G + B) / 3.0
    
    # Saturation calculation
    min_RGB = np.minimum(np.minimum(R, G), B)
    S = 1 - (3 / (R + G + B + 1e-6)) * min_RGB
    
    # Hue calculation
    numerator = 0.5 * ((R - G) + (R - B))
    denominator = np.sqrt((R - G) ** 2 + (R - B) * (G - B))
    theta = np.arccos(numerator / (denominator + 1e-6))
    H = np.where(B <= G, theta, 2 * np.pi - theta)
    H = H / (2 * np.pi)  # Normalize H to be in the range [0, 1]
    
    # Combine H, S, and I into one image
    hsi_image = np.stack((H, S, I), axis=-1)
    return hsi_image

def hsi_to_rgb(image):
    # Separare i canali H, S, I
    H, S, I = image[:,:,0], image[:,:,1], image[:,:,2]
    H = H * 2 * np.pi  # Convertire H da [0, 1] a [0, 2π]

    # Inizializzare i canali R, G, B
    R = np.zeros_like(H)
    G = np.zeros_like(H)
    B = np.zeros_like(H)

    # Maschere per le diverse regioni di H
    mask_0_120 = (H >= 0) & (H < 2 * np.pi / 3)
    mask_120_240 = (H >= 2 * np.pi / 3) & (H < 4 * np.pi / 3)
    mask_240_360 = (H >= 4 * np.pi / 3) & (H < 2 * np.pi)

    # Convertire i valori RGB per H tra 0 e 120 gradi
    R[mask_0_120] = I[mask_0_120] * (1 + S[mask_0_120] * np.cos(H[mask_0_120]) / np.cos(np.pi / 3 - H[mask_0_120]))
    B[mask_0_120] = I[mask_0_120] * (1 - S[mask_0_120])
    G[mask_0_120] = 3 * I[mask_0_120] - (R[mask_0_120] + B[mask_0_120])

    # Convertire i valori RGB per H tra 120 e 240 gradi
    H[mask_120_240] -= 2 * np.pi / 3
    G[mask_120_240] = I[mask_120_240] * (1 + S[mask_120_240] * np.cos(H[mask_120_240]) / np.cos(np.pi / 3 - H[mask_120_240]))
    R[mask_120_240] = I[mask_120_240] * (1 - S[mask_120_240])
    B[mask_120_240] = 3 * I[mask_120_240] - (R[mask_120_240] + G[mask_120_240])

    # Convertire i valori RGB per H tra 240 e 360 gradi
    H[mask_240_360] -= 4 * np.pi / 3
    B[mask_240_360] = I[mask_240_360] * (1 + S[mask_240_360] * np.cos(H[mask_240_360]) / np.cos(np.pi / 3 - H[mask_240_360]))
    G[mask_240_360] = I[mask_240_360] * (1 - S[mask_240_360])
    R[mask_240_360] = 3 * I[mask_240_360] - (G[mask_240_360] + B[mask_240_360])

    # Combinare i canali R, G, B
    rgb_image = np.stack((R, G, B), axis=-1)
    
    # Convertire i valori da [0, 1] a [0, 255]
    rgb_image = np.clip(rgb_image * 255, 0, 255).astype(np.uint8)
    return rgb_image


# def showSpectrum(x, descrizione):
    
# Esempio di utilizzo (supponendo che x sia un'immagine caricata):
# x = ml.leggiJPG("lena.jpg")
# y_filtered = gaussLPF(x, sigma=0.1)
# ml.showImage(y_filtered, "lena filtrata")


#def loc_equaliz(x):