import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics


a="E:\python_for_datascience\data\iris (1).csv"
df=pd.read_csv(a)
print(df.head())

print(df.Species.unique())
#Separating Features and Labels
X=df.iloc[:,1:5]
print(X)
y=df.iloc[:,5]
print(y)

#Train-Test Split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)

#Training Decision tree classifier

clf=DecisionTreeClassifier()
print(clf.fit(X_train,y_train))
y_predict=clf.predict(X_test)
print(y_predict)

#Evaluation Metric
accuracy=metrics.accuracy_score(y_test,y_predict)
print("Accuracy :",accuracy)
