import numpy as np
import pandas as pd
from pandas import Series,DataFrame

from pandas.plotting import scatter_matrix

import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sns

rcParams['figure.figsize']=5,4
sns.set_style('whitegrid')

#Eyeballing dataset distributions with histograms

address="E:\python_for_datascience\data\mtcars.csv"
cars=pd.read_csv(address)
cars.columns=['car_names','mpg',  'cyl',   'disp',   'hp',  'drat',     'wt',   'qsec',  'vs',  'am',  'gear',  'carb']
print(cars.head())
cars.index=cars.car_names
mpg=cars['mpg']
mpg.plot(kind='hist')
plt.show()
#Another way to plot histogram
plt.hist(mpg)
plt.show()
#Using seaborn way to plot histogram
sns.displot(mpg)
plt.show()

#Scatterplots
cars.plot(kind='scatter',x='hp',y='mpg',c=['darkgray'],s=150)
plt.show()

sns.regplot(x='hp',y='mpg',data=cars,scatter=True)
plt.show()

#Generating a scatter plot matrix
sns.pairplot(cars)
plt.show()

cars_subset=cars[['mpg','disp','hp','wt']]
sns.pairplot(cars_subset)
plt.show()

#Building boxplots
cars.boxplot(column='mpg',by='am')
cars.boxplot(column='wt',by='am')
plt.show()

#boxplots using seaborn
sns.boxplot(x='am',y='mpg',data=cars,hue='am',palette='hls')
plt.show()