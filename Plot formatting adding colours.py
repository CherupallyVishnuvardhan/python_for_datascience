import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series,DataFrame
from pylab import rcParams

import seaborn as sb

rcParams['figure.figsize']=5,4
sb.set_style('whitegrid')

#DEFINING PLOT COLOR
x=range(1,10)
y=[1,2,3,4,0.5,4,3,2,1]
plt.bar(x,y)
plt.show()

wide=[0.1,0.9,0.5,0.1,0.7,0.3,0.8,0.2,0.9]
color=['salmon']
plt.bar(x,y,width=wide,color=color,align='center')
plt.show()

address='E:\python_for_datascience\data\mtcars.csv'

cars=pd.read_csv(address)
print(cars)

cars.columns=['car_names','mpg',  'cyl',   'disp',   'hp',  'drat',     'wt',   'qsec',  'vs',  'am',  'gear',  'carb']
print(cars.head())

df=DataFrame(cars[['cyl','mpg','wt']])
df.plot()
plt.show()

color_theme=['darkgray','lightsalmon','powderblue']
df.plot(color=color_theme)
plt.show()

z=[1,2,3,4,0.5]
plt.pie(z)
plt.show()

#RGB CODES FOR THE COLOR FORMATTING

color_theme=['#A9A9A9','#FFA07A','#B0E0E6','#FFE4C4','#BDB76B']
plt.pie(z,colors=color_theme)
plt.show()

#Customizing line styles

x1=range(1,10)
y1=[9,8,7,6,5,4,3,2,1]
plt.plot(x,y)
plt.plot(x1,y1)
plt.show()

plt.plot(x,y,ls='solid',lw=5)
plt.plot(x1,y1,ls='--',lw='10')
plt.show()

#Setting plot markers

plt.plot(x,y,marker='1',mew=20)
plt.plot(x1,y1,marker='+',mew=10)
plt.show()