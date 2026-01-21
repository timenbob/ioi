import pandas as pd
import json

df = pd.read_csv("/home/timen/Documents/Faks/ioi/dn2/data 2gi del/1817602S_20251026-124305.csv", header=None,encoding="cp1250")

years = df.iloc[0, 1:].tolist()              # "1996","1997",...
values = df.iloc[1, 1:].tolist()             # 9582.000, 9971.000, ...

out = pd.DataFrame({
    "leto": pd.to_numeric(years),
    "poraba": pd.to_numeric(values)
})

out.to_json("energija.json", orient="records", date_format="iso", indent=2)


