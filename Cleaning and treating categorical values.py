import numpy as np
from pandas import DataFrame

from sklearn.preprocessing import LabelEncoder , OneHotEncoder

data={'names':['Vishnu','Vamshi','Aishu','Rjeev','Pradeep','Sathvika','Deepika'],
      'age':[24,25,26,21,22,23,28],
      'gender':['Male','Male','Female',np.nan,'Male',np.nan,'Female'],
      'rank':[3,1,2,4,7,6,5]}

df=DataFrame(data)
print(df)

df=df.drop('gender',axis=1)
print(df)

label_encoder=LabelEncoder()
label_encoder.fit(df['names'])
label_encoded_names=label_encoder.transform(df['names'])
print(label_encoded_names)


#One Hot Encoder
onehot_encoder=OneHotEncoder(sparse_output=False)
print(onehot_encoder.fit(df[['names']]))

onehot_encoded_names=onehot_encoder.transform(df[['names']])
onehot_encoded_df=DataFrame(onehot_encoded_names,columns=onehot_encoder.categories_)
onehot_encoded_df['names']=df[['names']]
print(onehot_encoded_df)