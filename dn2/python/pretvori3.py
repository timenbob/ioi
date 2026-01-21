import pandas as pd

# preberi izvorne podatke
df = pd.read_json("poraba_hrane.json")

# poskrbi da je stolpec kolicina številen
df["kolicina"] = pd.to_numeric(df["kolicina"], errors="coerce")

# seštej količino po letu
total = df.groupby("leto", as_index=False)["kolicina"].sum()

# preimenuj za lepši izvoz
total = total.rename(columns={"kolicina": "skupna_poraba"})

# shrani v nov JSON
total.to_json("poraba_hrane_skupno.json", orient="records", indent=2, force_ascii=False)

print("✓ Shrani: poraba_hrane_skupno.json")
