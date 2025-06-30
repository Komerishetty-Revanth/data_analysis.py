import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('sales.csv')
print(df.head())
grouped = df.groupby('Product')['Sales'].sum()
grouped.plot(kind='bar', title='Total Sales by Product', xlabel='Product', ylabel='Total Sales', figsize=(10, 6), color='skyblue')
plt.tight_layout()
plt.show()
