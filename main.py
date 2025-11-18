import pandas as pd

df = pd.read_csv("https://s3-eu-west-1.amazonaws.com/shanebucket/downloads/uk-500.csv")

print(df.head())
print(df.info())

print(df.address)