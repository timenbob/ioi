# merge_triple.py
import pandas as pd

# poti do datotek
ENERGIJA = "/home/timen/Documents/Faks/ioi/dn2/data/energija.json"                   # { "leto": 1996, "poraba": 9582.0 }
CENE     = "/home/timen/Documents/Faks/ioi/dn2/data/cene_hrane_povprecje.json"       # { "leto": 2018, "povprecna_cena": 3.63 }
PORABA   = "/home/timen/Documents/Faks/ioi/dn2/data/poraba_hrane_skupno.json"        # { "leto": 2000, "skupna_poraba": 708.4 }

# preberi
df_e = pd.read_json(ENERGIJA)
df_c = pd.read_json(CENE)
df_p = pd.read_json(PORABA)

# očisti tipe
for df in (df_e, df_c, df_p):
    df["leto"] = pd.to_numeric(df["leto"], errors="coerce").astype("Int64")

df_e = df_e.rename(columns={"poraba": "energija_gwh"})
df_c = df_c.rename(columns={"povprecna_cena": "povprecna_cena_eur"})
df_p = df_p.rename(columns={"skupna_poraba": "poraba_hrane_kg"})

# združi (outer join po letu) in uredi
out = (df_e.merge(df_c, on="leto", how="outer")
           .merge(df_p, on="leto", how="outer")
           .sort_values("leto")
           .reset_index(drop=True))

# opcijsko: zaokroži
out["povprecna_cena_eur"] = out["povprecna_cena_eur"].round(3)
out["poraba_hrane_kg"]    = out["poraba_hrane_kg"].round(3)
out["energija_gwh"]       = out["energija_gwh"].round(3)

# shrani
out.to_json("triple_merged.json", orient="records", indent=2, force_ascii=False)
print("✓ triple_merged.json zapisano,", len(out), "vrstic")
