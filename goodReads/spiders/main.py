import pandas as pd

pd.set_option("display.max_columns",None)
df = pd.read_json("C:/Users/LENOVO/PycharmProjects/pythonProject/goodReads/books.json")

df=df.set_index("title")


print(df.head())
print(df.describe())
print(df.shape)
print(df.info())

#Drop Null values
df=df.dropna()

df.to_csv("C:/Users/LENOVO/Downloads/Data analysis/goodReads_analysis/goodReads.txt")



