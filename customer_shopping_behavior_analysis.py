import pandas as pd
df = pd.read_csv("customer_shopping_behavior.csv")
print(df.head())
print(df.info())
print(df.describe(include='all'))
print(df.isnull().sum())