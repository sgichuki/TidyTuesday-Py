# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 21:42:01 2021

@author: warau
"""
from datetime import datetime 
import pandas as pd
import matplotlib.pyplot as plt 

#Load files
tarifbase = pd.read_excel(r'C:\Users\warau\Documents\python_work\TidyTuesdayPy\gazfrance/tarifBase.xlsx')
tarifb0 = pd.read_excel(r'C:\Users\warau\Documents\python_work\TidyTuesdayPy\gazfrance\tarifB0.xlsx')
tarifb1 = pd.read_excel(r'C:\Users\warau\Documents\python_work\TidyTuesdayPy\gazfrance\tarifB1.xlsx')

# multiple line plots
plt.plot( 'DATE_FIN', 'PART_FIXE_TTC', data=tarifbase, color= 'mediumblue', linewidth=2,label = "Tarif BASE")
plt.plot( 'DATE_FIN', 'PART_FIXE_TTC',data=tarifb0, color='red', linewidth=2, label = "Tarif B0")
plt.plot( 'DATE_FIN', 'PART_FIXE_TTC', data=tarifb1, color='olivedrab', linewidth=2, label = "Tarif B1")

plt.title("Natural gas prices in France 2013 - 2021")
plt.ylabel("price per kWh (Euros)")
plt.legend()

# use parameter bbox_to_anchor to reposition
# the legend box outside the plot area
plt.gca().legend(loc='center left', bbox_to_anchor=(1, 0.5))






