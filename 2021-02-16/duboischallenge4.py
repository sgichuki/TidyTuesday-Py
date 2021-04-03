import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns

#Load data 
slaves = pd.read_csv("freed_slaves.csv")

#Create axes object 
#ax = plt.axes()

fig,ax = plt.subplots()

#Create line plot 
sns.lineplot('Year','Slave',data=slaves, color = "seagreen")

#Put axis labels and tick marks at the top of the plot 
ax.xaxis.set_label_position('top') 
ax.xaxis.set_ticks_position('top')
ax.tick_params(labelbottom=False,labeltop=True)

#Label x and y axes 
ax.set_xlabel("Year",fontsize = 12)
ax.set_ylabel("Slaves",fontsize = 12)

#Fill area with black 
plt.fill_between('Year','Slave', data=slaves,color='black')

#Annotate the plot  
ax.annotate(text='SLAVES\nESCLAVES', xy=(1820,60), xycoords='data',color="bisque",fontsize = 16)
ax.annotate(text='FREE - LIBRE', xy=(1820,92), xycoords='data',color="black",fontsize = 12)

#Include plot title 
ax.set_title("PROPORTION OF FREEMEN AND SLAVES AMONG AMERICAN NEGROES.\n\nPROPORTION DES NEGRES LIBRES ET DES ESCLAVES EN AMERIQUE.\n\n DONE BY ATLANTA UNIVERSITY.")

#Label all the points Year/% of Slaves
ax.annotate(text='8%', xy=(1791,93), xycoords='data',color="black",fontsize = 9)
ax.annotate(text='11%', xy=(1801,90), xycoords='data',color="black",fontsize = 9)
ax.annotate(text='13.5%', xy=(1811,88), xycoords='data',color="black",fontsize = 9)
ax.annotate(text='13%', xy=(1821,88), xycoords='data',color="black",fontsize = 9)
ax.annotate(text='14%', xy=(1831,87.5), xycoords='data',color="black",fontsize = 9)
ax.annotate(text='13%', xy=(1841,88), xycoords='data',color="black",fontsize = 9)
ax.annotate(text='12%', xy=(1851,89.5), xycoords='data',color="black",fontsize = 9)
ax.annotate(text='11%', xy=(1861,90), xycoords='data',color="black",fontsize = 9)
ax.annotate(text='100%', xy=(1868,90), xycoords='data',color="black",fontsize = 9)

#Make the plot backgrouund green 
ax.set_facecolor('forestgreen')

#Insert grid lines
ax.grid (linewidth='0.4',color="grey")

#plt.show()

#Save the plot 
plt.savefig('slaves_plotPy.png',bbox_inches='tight')