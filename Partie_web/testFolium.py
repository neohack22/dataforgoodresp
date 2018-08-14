# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 10:42:14 2018

@author: nisha
"""

import folium

#%%
fond = r'http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png'
carte = folium.Map(location=[46.5, 2.3], zoom_start=6, tiles=fond, attr='© OpenStreetMap © CartoDB')
carte.create_map(path='/chemin/de/sortie/macarte.html')

#%%