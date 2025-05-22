import numpy as np
import pandas as pd

address="E:\python_for_datascience\data\mtcars.csv"
cars=pd.read_csv(address)
cars.columns=['car_names','mpg',  'cyl',   'disp',   'hp',  'drat',     'wt',   'qsec',  'vs',  'am',  'gear',  'carb']
cars.index=cars.car_names
print(cars.head(15))

carb=cars.carb
print(carb.value_counts())

cars_cat=cars[['cyl','vs','am','gear','carb']]
print(cars_cat.head())

gears_group=cars_cat.groupby('gear')

print(gears_group.describe())

#Transforming variables to categorical data type

cars['group']=pd.Series(cars.gear,dtype='category')
cars['group'].dtypes
x=cars['group'].value_counts()
print(x)

#Describing categorical data with crosstabs
print(pd.crosstab(cars['am'],cars['gear']))