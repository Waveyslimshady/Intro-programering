# Exempel - räkna antal 'a' i en text
text = "13324343532611465515256554532451154255241636666454"

antalA = 0

for bokstav in text:
    if bokstav == '6':
        antalA = antalA + 1

print('antal a:', antalA)
# utskriften blir:
# antal a: 2