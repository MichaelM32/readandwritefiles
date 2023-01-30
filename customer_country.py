import pandas as pd

df = pd.read_csv('customers.csv')
customer_country = ['FirstName', 'LastName', 'Country']


df.to_csv("customer_country.csv", index=False, columns=customer_country)
