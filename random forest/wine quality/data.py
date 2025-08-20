import pandas as pd

# Load Red Wine dataset
url_red = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
df_red = pd.read_csv(url_red, sep=";")   # use ; because values are separated by semicolons
print("Red Wine Dataset:")
print(df_red.head())

