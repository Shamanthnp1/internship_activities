import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dataset.csv")

df.head()
df.tail()
df.shape
df.info()
df.describe()

sns.histplot(df['age'], kde=True)
plt.show()

sns.boxplot(x=df['salary'])
plt.show()

df['gender'].value_counts()

sns.scatterplot(x='age', y='salary', data=df)
plt.show()

sns.boxplot(x='gender', y='salary', data=df)
plt.show()

corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()

sns.boxplot(x=df['salary'])
plt.show()
