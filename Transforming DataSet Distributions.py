import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, scale

address="E:\python_for_datascience\data\mtcars.csv"
df=pd.read_csv(address)
print(df.head())
plt.plot(df['mpg'])
plt.show()
#Normalization

minmax_scaler=MinMaxScaler()
print(minmax_scaler.fit(df[['mpg']]))

scaled_data=minmax_scaler.transform(df[['mpg']])
plt.plot(scaled_data)
plt.show()

#Standardization
standard_scaler=scale(df[['mpg']])
plt.plot(standard_scaler)
plt.show()