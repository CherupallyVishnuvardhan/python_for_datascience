import numpy as np
import pandas as pd
from pandas import DataFrame
numbers_df=DataFrame(np.arange(0,90,3).reshape(10,3),index=['row1','row2','row3','row4','row5','row6','row7','row8','row9','row10'],
                columns=['col1','col2','col3'])
print(numbers_df)
numbers_df.iloc[0,1]=20
print(numbers_df.iloc[0,1])
c=numbers_df.iloc[[1,2,6],[0,2]] 
print(c)
mask=numbers_df>30
print(mask)
print(numbers_df[mask])
numbers_df[numbers_df>30]=0
print(numbers_df)
print(numbers_df.iloc[0:6,0:2])
print(numbers_df.iloc[2:5,0:1])