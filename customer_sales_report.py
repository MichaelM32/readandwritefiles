import pandas as pd

df = pd.read_csv('sales.csv')
df2 = df.eval('Total = SubTotal + TaxAmt + Freight')
df2 = df2.groupby (['CustomerID'])['Total'].sum().reset_index()
print(df2)

df2.to_csv("salesreport.csv", index=False)