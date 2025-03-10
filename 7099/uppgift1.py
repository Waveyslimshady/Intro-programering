'''
kasta en sexsidig tärning 10 gånger
spara resultat i lista
sortera med minsta först
beräkna summan
beräkna medelvärde
ange minsta
ange största

räkna antalet sexor
vilken valör är vanligast? (svår)

skriv ut för att kontrollera att det blev rätt
'''
import random
min_lista = []
i = 0
while i < 10:
    print(i)
    tal = random.randint(1,6)

    min_lista.append(tal)
    i = i + 1
print (min_lista)
print('antal i listan', len(min_lista))
antal_1 = 0
for tal in min_lista:
    if tal == 1:
        antal_1 = antal_1 + 1
print ("summa:", sum (min_lista))
medel = sum (min_lista) / len(min_lista)
min_lista = sorted(min_lista)
print('antal ettor', antal_1) 
print(min_lista)
print ("medel:", medel)
print ("min: ", min (min_lista))
print ("max:", max (min_lista))
antal_6 = 0
for tal in min_lista:
    if tal == 6:
        antal_6 = antal_6 + 1
print ('antal sexor',antal_6 )