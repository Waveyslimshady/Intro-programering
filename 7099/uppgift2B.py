import random
min_lista = []
i = 0
while i < 5:
    print(i)
    tal = random.randint(1,6)
    min_lista.append(tal)
    i = i + 1
print (min_lista)

antal_1 = 0
for tal in min_lista:
    if tal == 1:
        antal_1 = antal_1 + 1
    if antal_1 == 5:
        print ("Yatzy med ettor!")

antal_2 = 0
for tal in min_lista:
    if tal == 2:
        antal_2 = antal_2 + 1
    if antal_2 == 5:
        print ("Yatzy med tvåor!")

antal_3 = 0
for tal in min_lista:
    if tal == 3:
        antal_3 = antal_3 + 1
    if antal_3 == 5:
        print ("Yatzy med treor!")

antal_4 = 0
for tal in min_lista:
    if tal == 4:
        antal_4 = antal_4 + 1
    if antal_4 == 5:
        print ("Yatzy med fyror!")

antal_5 = 0
for tal in min_lista:
    if tal == 5:
        antal_5 = antal_5 + 1
    if antal_5 == 5:
        print ("Yatzy med femmor!")

antal_6 = 0
for tal in min_lista:
    if tal == 6:
        antal_6 = antal_6 + 1
    if antal_6 == 5:
        print ("Yatzy med sexor!")

else:
    print ("Inte yatzy")