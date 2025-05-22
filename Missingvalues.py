#Filling missing values using fillna(),replace(),interpolate() functions.
import numpy as np
import pandas as pd
from pandas import DataFrame
data={'names':["vishnu","vamshi","raadha","vaishu","vikram","sathvik","deepika"],
      'age':[23,24,25,19,23,25,26],'gender':['M','M','F','F','M','M','F'],'rank':[4,1,3,5,6,2,7]}
ranking_df=DataFrame(data)
print(ranking_df)
ranking_df.iloc[2:5,1]=np.nan
ranking_df.iloc[3:6,3]=np.nan
ranking_df.iloc[3,:]=np.nan
print(ranking_df)
print(ranking_df.isnull())
print(ranking_df.notnull())
bool_series=pd.isnull(ranking_df['age'])
print(bool_series)
print(ranking_df[bool_series])
print(ranking_df.fillna(0))
print(ranking_df.fillna(method='pad'))
print(ranking_df.fillna('vishnu'))
print(ranking_df.fillna(method='bfill'))
print(ranking_df)
print(ranking_df.interpolate(method='linear'))
print(ranking_df.dropna())
print(ranking_df.dropna(how='all'))
print(ranking_df.dropna(axis=1))
print(ranking_df.dropna(axis=0))