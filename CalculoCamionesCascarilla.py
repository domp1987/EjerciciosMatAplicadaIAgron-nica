# -*- coding: utf-8 -*-
"""
Created on Wed May 22 15:16:16 2024

@author: Diego O Mendez P (DOMP)

@domp1987

El software esta diseñado como apoyo docente o gestor de conocimiento, 
con la generación de datos para el ejercicio, e impresión de parciales de
resultado y la respuesta.

El ejercicio se plantea para un terreno de un área en hectares generada 
aleatoriamente, con una capa vegetal tambien aleatoriamente, y para una planta 
hipotetica que necesita una profundidad de la raiz, que debe ser completada con 
cascarilla que esta en pacas comprimida 3 veces, y que se transporta en camiones
y la respuesta es la cantidad de camiones a llenar.

Tambien se pide cálcular el valor de la cascarilla, teniendo presente que el
primer camión es cobrado con $1'500.000, y por cada paca adicional es cobrada 
a $22.000. Se usa una linealización


"""
import random

# Generador de Cantidades

VPaca = 1.2 * 0.5 * 0.5  # Volumén paca de cascartilla comprimida(m)
FactorCompresion = 3 # Sin comprimir la cascarilla son 3 veces
VCamión = 2.5 * 3 * 5 # Volumén de camión (m)
CostoUnCamion = 1500000 # valor en pesos
CostoPorPaca = 22000

AreaLote  = 6.5 #round(random.random() * 12 + 1, 2) # Rango de 1 a 13 ha
ProfundidadUtil = round(random.random() / 5 + 0.05, 2 ) # rango de 0.05 - 0.20 m
ProfundidadRadicular = round(random.random() + 0.2, 2 ) # rango de 0.20 - 1 m

print(AreaLote, ProfundidadUtil, ProfundidadRadicular)

print("Volumen para cascarilla")
print((AreaLote * 10000 * ProfundidadRadicular) - (AreaLote * 10000 * ProfundidadUtil))
print("Cantidad de pacas de cascarilla")
print(((AreaLote * 10000 * ProfundidadRadicular) - (AreaLote * 10000 * ProfundidadUtil)) / (VPaca * FactorCompresion))
print("Cantidad de pacas por camión")
print(VCamión / VPaca)
Costo2doCamion = ((VCamión / VPaca) * CostoPorPaca) + CostoUnCamion

print("Número de viajes de camiones")
NCargaCamion = (((AreaLote * 10000 * ProfundidadRadicular) - (AreaLote * 10000 * ProfundidadUtil)) / 
                 (VPaca * FactorCompresion)) / (VCamión / VPaca)

# print(Costo2doCamion, CostoUnCamion)
m = Costo2doCamion - CostoUnCamion
b = CostoUnCamion - m *1
#print(m, b)

CostoViaje = m * NCargaCamion + b

print(round(NCargaCamion,2), "Camiones, Costo $", round(CostoViaje,2))

