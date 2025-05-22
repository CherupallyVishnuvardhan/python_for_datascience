import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from pylab import rcParams

rcParams['figure.figsize']=5,4

address="E:\python_for_datascience\data\iris.data.csv"
df=pd.read_csv(filepath_or_buffer=address, header=None, sep=',')
df.columns=['Sepal Length','Sepal Width','Petal Legth', 'Petal Width','Species']

x=df.iloc[:,0:4].values
y=df.iloc[:,4].values
print(x)
print(y)
print(df[:5])

#Identifying outliers from Tukey boxplots

df.boxplot(return_type='dict')
plt.plot()
plt.show()

Sepal_width=x[:,1]
iris_outliers=(Sepal_width>4)
print(df[iris_outliers])

Sepal_width=x[:,1]
iris_outliers=(Sepal_width<2.05)
print(df[iris_outliers])

#Applying Tukey outlier labeling

pd.options.display.float_format='{:.1f}'.format
X_df=pd.DataFrame(x)
print(X_df.describe())