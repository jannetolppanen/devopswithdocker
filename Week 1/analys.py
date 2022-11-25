with open("porssisahko2021_15.txt", "r") as tiedosto:
    sanakirja = {}
    for rivi in tiedosto:
        rivi = rivi.replace("\n", "")
        pvm = rivi[1:11]
        price = rivi[22:]
        kellonaika = rivi[12:22]
        if rivi[1] != "D":
            if pvm not in sanakirja:
                sanakirja[pvm] = {}
            sanakirja[pvm][kellonaika] = price

for paiva in sanakirja:
    summa = 0
    for hinta in sanakirja[paiva].values():
        summa += float(hinta)
    print(paiva)
    print(summa/(len(sanakirja[paiva])))
    

