#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Esercizio 1.7.1
Realizzate l’enhancement globale dell’immagine con equalizzazione dell’istogramma, scrivendo la fun- 
zione function y = glob equaliz(x), e mostrate l’immagine elaborata
"""
import sys
sys.path.append('/Users/luketto/Desktop/II Semestre IV Anno/ESM/Esercizi/Librerie')
import MyLibrary as ml

    
x = ml.leggiJPG("quadrato.tif")
y = ml.glob_equaliz(x)

ml.showTwoImages(x, y, "Originale", "Modificata")