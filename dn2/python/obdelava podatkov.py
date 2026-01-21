import json
import pandas as pd
from shapely.geometry import shape   # pip install shapely

# 1) centroidi iz GeoJSON
g = json.load(open("/home/timen/Documents/Faks/ioi/dn2/data 2gi del/Obcine-epsg4326.geojson", encoding="utf-8"))
rows = []
for f in g["features"]:
    name = f["properties"]["OB_UIME"]
    lon, lat = shape(f["geometry"]).centroid.xy
    rows.append({"OB_UIME": name, "lon": float(lon[0]), "lat": float(lat[0])})
cent = pd.DataFrame(rows)

# 2) tvoji podatki (po občinah)
gostota = pd.read_json("/home/timen/Documents/Faks/ioi/dn2/data 2gi del/gostota_prebivalstva.json")   # polja: OB_UIME, density
studenti = pd.read_json("/home/timen/Documents/Faks/ioi/dn2/data 2gi del/studenti_obcine.json")      # polja: OB_UIME, students
gostota = gostota.rename(columns={"obcina": "OB_UIME", "populacija": "density"})
studenti = studenti.rename(columns={"obcina": "OB_UIME", "populacija": "students"})


# 3) združi vse v eno tabelo
metrics = (cent.merge(gostota, on="OB_UIME", how="left")
                .merge(studenti, on="OB_UIME", how="left"))
metrics.to_json("obcine_metrics.json", orient="records",
                force_ascii=False, indent=2)
print("✓ obcine_metrics.json")
