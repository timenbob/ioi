import pandas as pd

df = pd.read_csv("/home/timen/Documents/Faks/ioi/dn3/data/Brown bear Slovenia 1993-1999.csv")

# preveri strukturo
print(df.columns)
print(df.head())

# očisti / filtriraj relevantne stolpce
df_clean = df[[
    "timestamp", "location-long", "location-lat", 
    "individual-local-identifier"
]].dropna()

# pretvori timestamp v datum
df_clean["timestamp"] = pd.to_datetime(df_clean["timestamp"])
df_clean["year"] = df_clean["timestamp"].dt.year

# shrani v JSON za uporabo v Vega-Lite
df_clean.to_json("medvedi.json", orient="records")
