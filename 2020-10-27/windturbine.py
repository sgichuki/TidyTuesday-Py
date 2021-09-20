import pandas as pd
import matplotlib.pyplot as plt 

#Load the data
windturbines = pd.read_csv("windturbine.csv", encoding = 'latin-1')

maxhubheight = windturbines['hub_height_m'].max()
maxrotordiameter = windturbines['rotor_diameter_m'].max()
maxprojectcap = windturbines['total_project_capacity_mw'].max()


#Mean hub height 
meanhubheight = windturbines['hub_height_m'].mean()
meanprojectcap = windturbines['total_project_capacity_mw'].mean()

#Convert province_territory to factor 
windturbines['province_territory'] = windturbines['province_territory'].astype('category')

#How many turbines per province?
turbinesperprovince = windturbines.groupby('province_territory').agg({'province_territory':'count'})


#Rename columns 
turbinesperprovince.columns = ['turbines']

turbinesperprovince_sorted= turbinesperprovince.sort_values('turbines')


#Plot series 
turbinesperprovince_sorted.plot(kind='barh',color = ['green'],legend = False)
plt.title("Wind turbines per province")
plt.ylabel(" ")
plt.xlabel("No. of turbines")

#How is turbine capacity distributed across the projects? 
#windturbines = [windturbines['turbine_rated_capacity_k_w'].dropna()]

windturbines.hist(column='turbine_rated_capacity_k_w', bins = 7, grid = False, color = 'purple')
plt.title("Histogram of turbine rated capacity")
plt.ylabel(" ")
plt.xlabel("rated capacity kW")



