import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pandas import DataFrame
data={'names':['vishnu','vamshi','sathvik','priya','raadha','deepika','vikram'],
      'age':[23,24,25,22,21,20,26],
      'gender':['MALE','MALE','MALE','FEMALE','FEMALE','FEMALE','MALE'],
      'rank':[4,1,3,2,6,5,7]}
data_2={'names':['rahul','vamshi','sathvik','priya','raadha','deepika','vikram'],
      'age':[23,24,25,22,21,20,26],
      'gender':['MALE','MALE','MALE','FEMALE','FEMALE','FEMALE','MALE'],
      'rank':[4,1,3,2,6,5,7]}
df=DataFrame(data)
df_2=DataFrame(data_2)
print(df)

#BAR PLOT WITH MATPLOTLIB

plt.bar(df['names'],df['age'])
plt.xlabel('Names')
plt.ylabel('Age')
plt.title('Comparing Ages with matplotlib')
plt.show()

#BAR PLOT WITH SEABORN

plot=sns.barplot(data=df_2,x='names',y='age')
plot.set_title("Comparing ages with seaborn")
plt.show()

#LINE PLOT WITH MATPLOTLIB

plt.plot(df['names'],df['age'])
plt.xlabel('Names')
plt.ylabel('Age')
plt.title("Comparing ages with line plot using matplotlib")
plt.show()

#LINE PLOT WITH SEABORN

pt=sns.lineplot(data=df,x='names',y='age')
pt.set_title("Comparing ages with line plot using seaborn")
plt.show()

#PIE CHART WITH MATPLOTLIB

plt.pie(df['age'],labels=df['names'])
plt.title("PIE CHART WITH MATPLOTLIB")
plt.show()

#PIE CHART WITH SEABORN

color=sns.color_palette('pastel')[0:5]
plt.pie(df['age'],labels=df['names'],colors=color)
plt.title("PIE CHART WITH SEABORN")
plt.show()