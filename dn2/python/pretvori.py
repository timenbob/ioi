import csv, json

with open("/home/timen/Documents/Faks/ioi/dn2/studenti po opcinah.csv",encoding="cp1250") as f:
    reader = csv.reader(f)
    data = []
    i=0
    for row in reader:
        if i==1:
            if len(row) < 3:
                continue
            data.append({
                "obcina": row[1],
                "populacija": 0 if row[2] == '-' else float(row[2])
            })
        i=1

with open("studenti_obcine.json", "w") as f:
    json.dump(data, f, indent=2)


