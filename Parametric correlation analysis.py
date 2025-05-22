import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
from pylab import rcParams

import scipy
from scipy.stats import pearsonr

rcParams['figure.figsize']=8,4
sns.set_style("whitegrid")

address="E:\python_for_datascience\data\mtcars.csv"
cars=pd.read_csv(address)
cars.columns=['car_names','mpg',  'cyl',   'disp',   'hp',  'drat',     'wt',   'qsec',  'vs',  'am',  'gear',  'carb']
sns.pairplot(cars)
plt.show()

x=cars[['mpg','hp','qsec','wt']]
sns.pairplot(x)
plt.show()

#Using Scipy to calculate the  Pearson correlation coefficient

mpg=cars['mpg']
hp=cars['hp']
qsec=cars['qsec']
wt=cars['wt']

pearsonr_coefficient, p_value = pearsonr(mpg, hp)
print('PearsonR Correlation Coefficient %0.3f' % (pearsonr_coefficient))

pearsonr_coefficient, p_value = pearsonr(mpg, qsec)
print('PearsonR Correlation Coefficient %0.3f' % (pearsonr_coefficient))

pearsonr_coefficient, p_value = pearsonr(mpg, wt)
print('PearsonR Correlation Coefficient %0.3f' % (pearsonr_coefficient))

#Using Pandas to calculate the Pearson correlation coefficient

corr=x.corr()
print(corr)

#Using Seaborn to visulaize the Pearson correlation coefficient
sns.heatmap(corr, xticklabels=corr.columns.values, yticklabels=corr.columns.values)
plt.show()