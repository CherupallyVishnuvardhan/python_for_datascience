import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sns

rcParams['figure.figsize']=5,4
sns.set_style('whitegrid')

#Labeling plot features
#The functional method
x=range(1,10)
y=[4,3,2,1,0.5,4,3,2,1]
plt.bar(x,y)

plt.xlabel("your x-axis label")
plt.ylabel("your y-axis label")
plt.show()

z=[1,2,3,4,0.5]
veh_type=['car','van','bicycle','bike','bus']
plt.pie(z,labels=veh_type)
plt.show()

#Object oriented method
address="E:\python_for_datascience\data\mtcars.csv"
cars=pd.read_csv(address)
cars.columns=['car_names','mpg',  'cyl',   'disp',   'hp',  'drat',     'wt',   'qsec',  'vs',  'am',  'gear',  'carb']
mpg=cars.mpg

fig=plt.figure()
ax=fig.add_axes([.25,.25,0.5,0.5])
mpg.plot()
ax.set_xticks(range(32))
ax.set_xticklabels(cars.car_names,rotation=60,fontsize='medium')
ax.set_title('Miles per gallon of cars in mtcars')
ax.set_xlabel('car names')
ax.set_ylabel('miles/gal')
plt.show()

#Adding a legend to a plot
#The Functional Method
plt.pie(z)
plt.legend(veh_type,loc='best')
plt.show()

#The object oriented method
fig=plt.figure()
ax=fig.add_axes([0.25,0.25,0.5,0.5])
mpg.plot()
ax.set_xticks(range(32))
ax.set_xticklabels(cars.car_names,rotation=60,fontsize='medium')
ax.set_title('Miles per gallon of cars in mtcars using legends')
ax.set_xlabel('car names')
ax.set_ylabel('miles/gal')
ax.legend(loc='best')
plt.show()

#Annotating your plot
print(mpg.max())
fig=plt.figure()
ax=fig.add_axes([0.25,0.25,0.5,0.5])
mpg.plot()
ax.set_xticks(range(32))
ax.set_xticklabels(cars.car_names,rotation=60,fontsize='medium')
ax.set_title('Miles per gallon of cars in mtcars using Annotation')
ax.set_xlabel('car names')
ax.set_ylabel('miles/gal')
ax.set_ylim([0,45])
ax.annotate('Toyota Corolla',xy=(19,33.9),xytext=(21,35),arrowprops=dict(facecolor='black',shrink=0.05 ))
ax.legend(loc='best')
plt.show()
