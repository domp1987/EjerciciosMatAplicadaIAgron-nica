# -*- coding: utf-8 -*-
"""
Created on Fri May 24 17:58:31 2024

@author: Portatil
"""

# Ejercicio de café

import random

PlantasCafe = round(random.random() * 13000 + 100, 2) # Rango de 100 a 130000 ha (150)
CantidadCargas = round(random.random() * 55 + 1, 2) # Rango de 1 a 55 ha (1)
DSiembra = round(random.random() * 10000 + 100, 2) # Rango de 100pl/ha a 10000 pl/ha (10000)
ProdHa = round(random.random() * 9000 + 1000, 2) # Rango de 1000 a 9000 kg (8000)

print(PlantasCafe, CantidadCargas, DSiembra, ProdHa)
RendimientoPlanta = ProdHa / DSiembra # Kilogramos por planta
ProdEsperada = RendimientoPlanta * PlantasCafe# Producción Esperada


PesoCarga = CantidadCargas  * 150 # Una Carga 150 Kg
ProdReal =  PlantasCafe * (PesoCarga / PlantasCafe) # Peso por planta kg/pl

print("Producción cultivo esperada", ProdEsperada, "Producción en peso", ProdReal)



