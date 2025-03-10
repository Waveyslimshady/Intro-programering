Våge Kjellman logbok
===
2025-03-10
----------

2025-03-03
----------
For slingor...
Det är en slinga som loopar
tillexempel:
mening = input ("Skriv en mening.")


    for diff in range(1,27):
        output = ""
        for bokstav in mening:
            if bokstav == '_':
                output = output + '_'
            else: 
                tal= ord (bokstav)

                tal = tal - diff
                if tal < 97:
                    # aj aj för lite
                    tal =tal +26
                chr (tal)
                output = output + (chr(tal))
        print (output)
        print()

Denna koden ska krytera en text genom att mata in en kryterad text. Slingan loopar 26 gånger, Det bärettar för programet att hur mycket varje bokstav ska sliftas för att knäcka den krypterade texten eller meningen. Sen så har vi uteslutigt blankslag och gjort så att den visas som "_" i resultatet. Sedan flyttas alla bokstäver bak 26 gånger. Men vi har uteslutigt åäö i kryteringen då kryterade texten inte använde åäö. Denna koden tar meningen ifrån inputet och flyttar bak bostäverna 26 gånger i en for slinga. Och printar ut varje variation av meningen. så 26 variationer skrivs ut och den kryterade meningen gömmer sig i röran av alla olika variationer. Så det är jobbigt att hitta rätt kryptering.

01-10-2025
-------
Jag har nästan gjort klar alla uppgiter fram till 7070.


23-09-2024
-----
gjort:
7040
7045
7050 pågår
Nästan gjort 


30-08-2024
---
Jag har installrat allt nu.