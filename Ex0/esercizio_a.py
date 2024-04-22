#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Esercizio a
"""
import numpy as np

def clip(x, limit):
    """
    Dato un vettore x, satura i valori
    del vettore superiori a limit
    """
    for i in range (0, len(x)):
        if(x[i] > limit):
            x[i] = 0
            
    return x

V = np.array([-10, 3, -6, 0, 1, -2, 3, 4, -15, 3, 21])
clip(V, 8)
print(V)
    