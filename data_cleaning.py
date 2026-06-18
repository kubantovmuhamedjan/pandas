import pandas as pd

df = pd.read_csv("data.csv")

# 1. Drop irrelevant columns
# df = df.drop(columns=["Legendary"])

# 2. Handle missing data
# df = df.dropna(subset=["Type2"]) # осы бағандағы NA ларды өшіреді
# df = df.fillna({"Type2": "None"}) # осы бағандағы NA ларды NONE қылады бірақ өшірмейді

# 3. Fix inconsistent values
# df["Type1"]= df["Type1"].replace({"Grass": "GRASS", "Fire": "FIRE", "Water": "WATER"})

# 4. Standardize text
# df["Name"]=  df["Name"].str.lower()

# 5. Fix data types
# df["Legendary"] = df["Legendary"].astype(bool)

# 6. Remove duplicate  values
df = df.drop_duplicates()


print(df.to_string())