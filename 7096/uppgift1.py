# Exempel - räkna antal 'a' i en text
text = ""

antalA = 0

for bokstav in text:
    if bokstav == 'a':
        antalA = antalA + 1

print('antal a:', antalA)
# utskriften blir:
# antal a: 2