import pandas as pd

data = {"Name": ["Spongebob", "Patrick", "Squidward"],
        "Age": [30, 35, 50],
        }

df =  pd.DataFrame(data, index=["Empl 1", "Empl 2","Empl 3"])

print(df)

print("----------------------")
print(df.loc["Empl 3"])

print("---------------------")
print(df.iloc[1])

print("ADD NEW COLUMN ____________")
df["Job"] =["Cook", "N/A", "Cashier"]
print(df)

print("ADD NEW ROW -----------------")
new_row = pd.DataFrame([{"Name": "Sandy", "Age": 28, "Job": "Engineer"}], index=["Empl 4"])
df =pd.concat([df, new_row])
print(df)


