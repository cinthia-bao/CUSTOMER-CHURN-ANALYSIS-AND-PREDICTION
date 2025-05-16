#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 16 00:13:17 2025

@author: ale
"""

import pandas as pd
import matplotlib.pyplot as plt

train = pd.read_csv("dataset_modif/train_clean.csv")

columna = 'Exited'  
conteo = train[columna].value_counts()

# Imprimir cuántos hay de cada uno
print(f"Conteo de valores en la columna '{columna}':\n{conteo}")

# Gráfico de pastel
plt.figure(figsize=(6, 6))
plt.pie(conteo, labels=conteo.index, autopct='%1.1f%%', startangle=90)
plt.title(f'Distribución de {columna}')
plt.axis('equal') 
plt.show()
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

# Crear un GeoDataFrame manual con geometrías aproximadas
from shapely.geometry import Polygon

# Geometrías aproximadas (solo para demostración)
spain = Polygon([(-9, 36), (-9, 44), (4, 44), (4, 36)])
france = Polygon([(-5, 42), (-5, 51), (8, 51), (8, 42)])
germany = Polygon([(5, 47), (5, 55), (15, 55), (15, 47)])

data = {
    'name': ['Spain', 'France', 'Germany'],
    'value': [10, 20, 15],
    'geometry': [spain, france, germany]
}
gdf = gpd.GeoDataFrame(data)

# Crear el mapa
fig, ax = plt.subplots(figsize=(10, 6))
gdf.plot(column='value', ax=ax, legend=True,
        cmap='OrRd', edgecolor='black')
ax.set_title("Mapa Simplificado")
plt.show()