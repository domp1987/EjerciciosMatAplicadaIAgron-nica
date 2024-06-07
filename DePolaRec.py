# -*- coding: utf-8 -*-
"""
Created on Tue May 28 09:44:05 2024

@author: Portatil
"""
import numpy as np
MagA, MagB = 7, 5

AngA, AngB = 20, 70

x = MagA * np.cos(np.radians(AngA))
y = MagA * np.sin(np.radians(AngA))

print(x, y)

x = MagB * np.cos(np.radians(AngB))
y = MagB * np.sin(np.radians(AngB))

print(x, y)