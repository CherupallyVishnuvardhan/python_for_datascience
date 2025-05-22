#CONCATENATION

import numpy as np
import pandas as pd
from pandas import Series,DataFrame
DF_obj=DataFrame(np.arange(36).reshape(6,6))
print(DF_obj)
DF_obj_2=DataFrame(np.arange(15).reshape(5,3))
print(DF_obj_2)
print(pd.concat([DF_obj,DF_obj_2],axis=1))
print('/n')
print(pd.concat([DF_obj,DF_obj_2],axis=0))
print(pd.concat([DF_obj,DF_obj_2]))

#DROPPING_DATA

print(DF_obj.drop([0,3]))  #it is for rows

print(DF_obj.drop([0,2],axis=1))  #it is for columns

#ADDING_DATA

series_obj=Series(np.arange(5))
series_obj.name='ADDING_VARIABLE'
print(series_obj)

variable_added=DataFrame.join(DF_obj,series_obj)
print(variable_added)

added_datatable=pd.concat([variable_added,variable_added],ignore_index=False)

print(added_datatable)

print(pd.concat([DF_obj_2,series_obj],axis=0))
print(pd.concat([DF_obj_2,series_obj],axis=1))

added_datatable=pd.concat([variable_added,variable_added],ignore_index=True)
print(added_datatable)


#SORTING

DF_sorted=DF_obj.sort_values(by=[5],ascending=[False])
print(DF_sorted)
DF_sorted=DF_obj.sort_values(by=[3],ascending=False)
print(DF_sorted)