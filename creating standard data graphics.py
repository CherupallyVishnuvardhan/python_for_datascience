import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas import DataFrame
from numpy.random import randn
from matplotlib import rcParams

#Line plot
x=range(1,10)
y=[1,2,3,4,0,4,3,2,1]
plt.plot(x,y)
plt.show()

address="E:\python_for_datascience\data\mtcars.csv"
data=pd.read_csv(address)
data.columns=['car_names','mpg',  'cyl',   'disp',   'hp',  'drat',     'wt',   'qsec',  'vs',  'am',  'gear',  'carb']
mpg=data['mpg']
mpg.plot()
plt.show()
data.plot()
plt.show()
df=data[['cyl','wt','mpg']]
df.plot()
plt.show()

#Bar plot
plt.bar(x,y)
plt.show()

#creating bar plots from pandas object
mpg.plot(kind='area')
plt.show()
mpg.plot(kind='bar')
plt.show()

#creating pie charts
x=[1,2,3,4,0,2,3,4,5]
plt.pie(x)
plt.savefig('pie_chart.png')
plt.show()