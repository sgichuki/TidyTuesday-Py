# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 14:19:31 2021

@author: warau
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

UKnewcars = pd.DataFrame({
    'Model':["Diesel", "MHEV Diesel", "Petrol", "MHEV petrol","BEV", "PHEV", "HEV"],
    '2020':[209093,44351,719908,77423,66611,42483,83787],
    '2021':[117605,85171,621598,159776,125141,87040,120283]})



UKnewcars_change = UKnewcars.set_index('Model').pct_change(axis=1)*100

# displaying the results
print(UKnewcars_change.to_string(index = True))

UKnewcars.plot(x = "Model", y =["2020","2021"], kind = "bar")
plt.xticks(rotation = 45)
plt.xlabel(" ")
plt.ylabel("Car registrations")
plt.title("New car registrations in the U.K")



