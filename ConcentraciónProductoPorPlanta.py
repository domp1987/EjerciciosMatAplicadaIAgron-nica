# -*- coding: utf-8 -*-
"""
Created on Fri May 24 17:24:09 2024

@author: Portatil
"""
import random

ACultivada = round(random.random() * 12 + 1, 2) # Rango de 1 a 13 ha
PresentGramos = round(random.random() * 3000 + 500, 2) # Rango de 500 a 3000 gr
PresentLitros = round(random.random() * 3 + 0.5, 2) # Rango de 0.5 a 3 L
DSiembra = round(random.random() * 900000 + 500, 2) # Desnsidad 500 - 900000 pl/ha
CCompradaUn = round(random.random() * 10 + 1, 2) # Rango 1 a 8 un
CHidricoPlanta = round(random.random() + 0.2, 2) # Rango de 0.2 a 1 L al día

CPlantas = DSiembra * ACultivada
CHidriTot = CHidricoPlanta * CPlantas
ConcProduc = PresentGramos / PresentLitros # Concentración por L

print(ACultivada, PresentGramos,PresentLitros, DSiembra, CCompradaUn, CHidricoPlanta)
print("Concentración producto por cada litro", ConcProduc)
print("Cantidad de plantas", CPlantas, "Consumo Hídrico Total L", CHidriTot)

Concentración = (CCompradaUn * PresentGramos) / CHidriTot
ConcPlanta = Concentración * CHidricoPlanta

print(" Concentración total en agua mg/L", Concentración * 1000)
print("Concentracion por planta mg/pl", ConcPlanta * 1000)



