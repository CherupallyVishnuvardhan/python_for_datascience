import numpy as np
import pandas as pd
from pandas import Series,DataFrame

from pylab import rcParams
import seaborn as sns
rcParams['figure.figsize']=5,4
sns.set_style('whitegrid')

import scipy
from scipy import stats

address='E:\python_for_datascience\data\mtcars.csv'
cars=pd.read_csv(address,encoding='cp1252',parse_dates=True)
print(cars)
cars.columns=['car_names', 'mpg',  'cyl',   'disp',   'hp',  'drat',     'wt',   'qsec',  'vs',  'am',  'gear',  'carb']
print(cars.sum())
x=cars.sum(axis=1,numeric_only=True)
print(x)
y=cars.median(numeric_only=True)
print(y)
print(cars.max())
mpg=cars.mpg
print(mpg.idxmax())

#Looking at summary statistics that describe variable distribution

z=cars.std(numeric_only='True')
print(z)

m=cars.var(numeric_only='True')
print(m)

gear=cars.gear
print(gear.value_counts())

print(cars.describe())