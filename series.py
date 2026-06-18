import pandas as pd

data = [100, 102, 104, 200, 202]
series = pd.Series(data, index=["a", "b", "c", "d", "e"])

# series.loc["c"] = 200

print(series.loc["a"])  # 100

print(series.iloc[0])

print(series)

print(series[series >= 200])

calories = {"Day 1": 1750, "Day 2": 2100, "Day 3": 1700}

seriess = pd.Series(calories)
print(seriess)
