import pandas as pd

df = pd.read_csv("data.csv", index_col="Name")

#SELECTION BY COLUMN
# print(df["Name"].to_string())
# print(df["Height"].to_string())
# print(df["Weight"].to_string())
# print(df[["Name", "Weight", "Height"]].to_string())

# SELECTION BY ROWS
# print(df.loc["Pikachu", ["Height", "Weight"]])
# print(df.iloc[0:11:2,  0:3])

pokemon = input("Enter a Pokemon name:")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found")
