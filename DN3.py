import json

with open(r'C:\Users\tilen\Desktop\TP\MOJE VAJE\DN3\zacetniData', 'r') as zacetna_file:
    zacetniData = json.load(zacetna_file)

with open(r'C:\Users\tilen\Desktop\TP\MOJE VAJE\DN3\updateData', 'r') as posodobitev_file:
    updateData = json.load(posodobitev_file)

zacetni_slovar = {oseba['name']: oseba for oseba in zacetniData['persons']}

for oseba in updateData['persons']:
    ime = oseba['name']
    if ime in zacetni_slovar:
        zacetni_slovar[ime].update(oseba)


zacetni_slovar = list(zacetni_slovar.values())

posodobljena_datoteka = {'persons': zacetni_slovar}

with open(r'C:\Users\tilen\Desktop\TP\MOJE VAJE\DN3\nova', 'w') as izhodna_file:
    json.dump(posodobljena_datoteka, izhodna_file, indent=2)
