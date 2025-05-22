import pandas as pd
import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sns

rcParams['figure.figsize']=5,4
sns.set_style('whitegrid')

address="E:\python_for_datascience\data\iris.data.csv"
df=pd.read_csv(filepath_or_buffer=address, header=None, sep=',')
df.columns=['Sepal Length','Sepal Width','Petal Legth', 'Petal Width','Species']

print(df)

x=df.iloc[:,0:4].values
print(x)

y=df.iloc[:,4].values
print(y)

print(df[:5])

sns.boxplot(x='Species',y='Sepal Length',data=df,hue='Species',palette='hls',legend=False)
plt.show()

sns.pairplot(df,hue='Species',palette='hls')
plt.show()

#Applying Tukey Outlier Labelling

pd.options.display.float_format='{:.1f}'.format
X_df=pd.DataFrame(x)
print(X_df.describe())

