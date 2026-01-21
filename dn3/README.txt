Podatke dobimo v dveh tabelah.
Prva vsebuje vse meritve, ki so jih senzorji zabeležili skozi čas. Za naš namen so ključni naslednji podatki:

* čas meritve (timestamp),

* geografska lokacija (location-long, location-lat),

* oznaka posameznega medveda (individual-local-identifier).

Druga tabela vsebuje dodatne informacije o posameznih medvedih. Teh podatkov nismo uporabili, saj niso bili potrebni za izbrano vizualizacijo.

Pri pretvorbi prve tabele iz CSV v JSON smo podatke najprej očistili. Odstranili smo vse stolpce, ki jih nismo potrebovali, ter ohranili samo: ime medveda, čas meritve in lokacijo. Dodali smo tudi izračunano leto (year), ki pa se je izkazala za nepotrebno.

Da poženemo part_3.html rabimo server(8080)
Sem pa dodal še part_3_brez.html kjer ne rabimo serverja.