import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sns

rcParams['figure.figsize']=5,4
sns.set_style('whitegrid')

#The simplest time series plot
address="E:\python_for_datascience\data\Superstore-Sales.csv"
df1=pd.read_csv(address,encoding='cp1252')
print(df1)
df=pd.read_csv(address,index_col='Order Date',encoding='cp1252',parse_dates=True)
print(df.head())
df['Order Quantity'].plot()
plt.show()

df2=df.sample(n=100,random_state=25,axis=0)
plt.xlabel('Order Date')
plt.ylabel('Order Quantity')
plt.title("Superstore Sales")
df2['Order Quantity'].plot()
plt.show()
