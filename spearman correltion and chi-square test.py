import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series , DataFrame
import seaborn as sns
from pylab import rcParams
import scipy
from scipy.stats import spearmanr

rcParams['figure.figsize']=14,7
sns.set_style("whitegrid")

address="E:\python_for_datascience\data\mtcars.csv"
cars=pd.read_csv(address)
cars.columns=['car_names','mpg',  'cyl',   'disp',   'hp',  'drat',     'wt',   'qsec',  'vs',  'am',  'gear',  'carb']
print(cars.head())

x=cars[['cyl','vs','am','gear']]
sns.pairplot(x)
plt.show()

cyl=cars['cyl']
vs=cars['vs']
am=cars['am']
gear=cars['gear']

spearmanr_coefficient, P_value=spearmanr(cyl,vs)
print("Spearman Rank Correlation coefficient %0.3f" % (spearmanr_coefficient))

spearmanr_coefficient, P_value=spearmanr(cyl,am)
print("Spearman Rank Correlation coefficient %0.3f" % (spearmanr_coefficient))

spearmanr_coefficient, P_value=spearmanr(cyl,gear)
print("Spearman Rank Correlation coefficient %0.3f" % (spearmanr_coefficient))

#Chi-Square Test

table=pd.crosstab(cyl,am)
from scipy.stats import chi2_contingency
chi2, p, dof, expected=chi2_contingency(table.values)
print('Chi-square Statistic %0.3f p_value %0.3f' %(chi2,p))

table=pd.crosstab(cyl,vs)

chi2, p, dof, expected=chi2_contingency(table.values)
print('Chi-square Statistic %0.3f p_value %0.3f' %(chi2,p))

table=pd.crosstab(cyl,gear)

chi2, p, dof, expected=chi2_contingency(table.values)
print('Chi-square Statistic %0.3f p_value %0.3f' %(chi2,p))