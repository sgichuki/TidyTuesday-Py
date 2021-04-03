import matplotlib.pyplot as plt 
import pandas as pd 

#Load the data
georgiapop = pd.read_csv("georgia_pop.csv")

#plot lines
fig,ax = plt.subplots()

#Setup the plot in the code below
#reverse the x axis
ax.invert_xaxis()

#include the grid lines in the plot
ax.grid (linewidth='0.4')

#Choose the color sandybrown for the plot background
ax.set_facecolor('sandybrown')

#Set limits for the y axis
plt.ylim(1790,1890)

#Draw lines for each column in the data
plt.plot('Colored','Year',data=georgiapop,linestyle='solid',color='black')
plt.plot('White','Year',data=georgiapop,linestyle='dashed',color='black')

#Put in a title for the plot 
ax.set_title("COMPARATIVE INCREASE OF WHITE AND COLORED POPULATION IN GEORGIA")

#Label the legend and place it at the bottom of the plot 
plt.legend(['Colored','White'],bbox_to_anchor = (0.5,-0.05))

#This command shows the plot in a pop up window 
#plt.show()

#Save the plot 
plt.savefig('georgiapop_plotPy.png',bbox_inches='tight')