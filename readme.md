Våge Kjellman logbok
===
2025-03-10
----------
if satser.

Denna if satsen berättar hur python ska behandla datan eller variablen och bearbeta den. så som att man matar in 58 så berättar den att det är ett två siffrigt tal. Och om man matar in 563 så berättar koden för dig att det är ett tre siffrigt tal. Så satsen går igenom olika typer av lösningar för att hitta rätt lösning som programeraren har anget.

    nummer = input ("Ge mig ett tal mellan 0 till 1000.")
    nummer = int (nummer)
    print(nummer)
    if nummer >=0 and nummer <=9:
        print ("ensiffrigt tal")
    elif nummer >=9 and nummer <=99:
        print ("tvåsiffrigt tal")
    elif nummer >=100 and nummer <=999:
        print ("tresiffrigt tal")
    elif nummer >=1000 and nummer <=9999:
        print ("Är minst fyrsiffriga tal.")
    elif nummer <=0:
        print ("Tal mindre än 0 är negativa.")

2025-03-03
----------
For slingor...
Det är en slinga som loopar
tillexempel:
mening = input ("Skriv en mening.")

<code>
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
</code>

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