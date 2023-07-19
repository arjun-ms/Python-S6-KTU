import pandas as pd

df = pd.read_csv('diamonds.csv')
print(df.head(5))
rows,columns = df.shape
print(rows)
print(columns)