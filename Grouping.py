import numpy as np
import pandas as pd
from pandas import DataFrame,Series

address='E:\python_for_datascience\data\mtcars.csv'

cars=pd.read_csv(address)
print(cars)

cars.columns=['car_names','mpg',  'cyl',   'disp',   'hp',  'drat',     'wt',   'qsec',  'vs',  'am',  'gear',  'carb']
print(cars.head())

cars_groups=cars.groupby(cars['cyl'])
print(cars_groups.mean(numeric_only=True))

cars_group=cars.groupby(cars['disp'])
print(cars_group.mean(numeric_only=True))