import pandas as pd
import numpy as np

# create df from a numpy array:
arr = np.random.randn(6, 4)
df1 = pd.DataFrame(arr, columns=list("ABCD"))

# create df from a dict
shop_articles = {
    "weight": [10.1, 5.0, 8.3, 7.2],
    "color": ["red", "green", "blue", "transparent"],
    "availability": [False, True, True, False],
    "price": 8.99  # all have the same price
}
article_numbers = ["A107", "A108", "A109", "A110"]
df2 = pd.DataFrame(shop_articles, index=article_numbers)

# each has its own data type
print("column types:\n", df2.dtypes)





fname = "things.csv"

# save the data frame as CSV file (Comma Separated Values )
# csv file will also contain header information (column labels)
df2.to_csv(fname)



# Pandas function to load csv-data into DataFrame
# (Detects column names automatically)
df2_new = pd.read_csv(fname)

# display(df2_new)  # Jupyter-Notebook-specific





# access individual values (by verbose index and column):
print(df2.loc["A108", "weight"])
df2.loc["A108", "weight"] = 3.4  # set new value
df2.loc["A108", "weight"] += 2  # increase by two

# access by numerical indices
print(df2.iloc[1, 0])  # row index: 1, column index: 0

# use slices to change multiple values
df2.loc["A108":"A109", "price"] *= 0.30  # 30% discount

# access multiple columns (-> new df object)
print(df2[["price", "weight"]])

# new column (-> provide a height value for every article)
df2["height"] = [10, 20, 30, 40]

# new row (-> provide a value for every column (weight, color, ...) )
df2.loc["X400"] = [15 , "purple" , True , 25.00 , 50]



# create Series-object with bool-entries
idcs = df2["weight"] > 8

# use this Series-object for indexing
print(df2[idcs])

# similar statement without intermediate variable:
print(df2[df2["weight"] < 8])


df2.describe()
df2["price"].mean()
df2["weight"].median()
df2["weight"].max()

print("shorthand notation (if column label is valid python name)")
print(df2.weight == df2["weight"])
print(all(df2.weight == df2["weight"]))

# combine function application with boolean indexing
df2[df2.weight>8].weight.mean()

# apply an arbitrary function (here np.diff) to each (selected) column
print(df2[["price", "weight"]].apply(np.diff))
