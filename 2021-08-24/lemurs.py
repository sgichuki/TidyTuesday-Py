# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 13:21:42 2021

@author: warau
"""
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt 

#load data 
lemurs = (
    pd.read_csv("https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-08-24/lemur_data.csv",encoding= 'unicode_escape'))

taxonomic_code = pd.read_csv("taxonomic_code.csv", encoding = 'Latin1')

#convert column names to lower case 
taxonomic_code.columns = taxonomic_code.columns.str.lower()

#merge data frames to associate species name to taxon code 

newlemurs = pd.merge(taxonomic_code, lemurs, on="taxon")

longevity = newlemurs[['common name','age_at_death_y']].groupby('common name').median()

longevity_sorted = longevity.sort_values('age_at_death_y')

#longevity.columns = longevity.columns.droplevel(0)

longevity_sorted.plot(kind='barh',color = ['green'],legend = False)
plt.title("Lemur longevity: median age at death by species")
plt.ylabel(" ")
plt.xlabel("Median age at death")





