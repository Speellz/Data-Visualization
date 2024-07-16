import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#örnek set
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Revenue': [15000, 18000, 17000, 16000, 21000, 22000, 19000, 23000, 20000, 25000, 24000, 26000],
    'Expenses': [5000, 6000, 5500, 7000, 7500, 8000, 6500, 8500, 7000, 9000, 8500, 9000]
}
df = pd.DataFrame(data)
df['Profit'] = df['Revenue'] - df['Expenses']

print(df)

print(df.describe())

#aylık gelir
plt.figure(figsize=(10, 6))
sns.lineplot(x='Month', y='Revenue', data=df, marker='o')
plt.title('Monthly Revenue')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.show()

#aylık gider
plt.figure(figsize=(10, 6))
sns.lineplot(x='Month', y='Expenses', data=df, marker='o', color='r')
plt.title('Monthly Expenses')
plt.xlabel('Month')
plt.ylabel('Expenses')
plt.xticks(rotation=45)
plt.show()

#aylık kar
plt.figure(figsize=(10, 6))
sns.lineplot(x='Month', y='Profit', data=df, marker='o', color='g')
plt.title('Monthly Profit')
plt.xlabel('Month')
plt.ylabel('Profit')
plt.xticks(rotation=45)
plt.show()

#hepsi
plt.figure(figsize=(10, 6))
sns.lineplot(x='Month', y='Revenue', data=df, marker='o', label='Revenue')
sns.lineplot(x='Month', y='Expenses', data=df, marker='o', color='r', label='Expenses')
sns.lineplot(x='Month', y='Profit', data=df, marker='o', color='g', label='Profit')
plt.title('Monthly Financial Overview')
plt.xlabel('Month')
plt.ylabel('Amount')
plt.xticks(rotation=45)
plt.legend()
plt.show()

#matris ve ısı haritası
correlation_matrix = df[['Revenue', 'Expenses', 'Profit']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()
