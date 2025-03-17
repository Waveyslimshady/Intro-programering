import random
min_lista = []
i = 0
while i < 5:
    print(i)
    tal = random.randint(1,1)
    min_lista.append(tal)
    i = i + 1
print (min_lista)

antal_1 = 1
for tal in min_lista:
    if tal == 1:
        antal_1 = antal_1 + 1
    if antal_1 == 5:
        print ("Yatzy!")

antal_2 = 2
for tal in min_lista:
    if tal == 1:
        antal_2 = antal_2 + 1
    if antal_2 == 5:
        print ("Yatzy!")

antal_3 = 3
for tal in min_lista:
    if tal == 1:
        antal_3 = antal_3 + 1
    if antal_3 == 5:
        print ("Yatzy!")

antal_4 = 4
for tal in min_lista:
    if tal == 1:
        antal_4 = antal_4 + 1
    if antal_4 == 5:
        print ("Yatzy!")

antal_5 = 5
for tal in min_lista:
    if tal == 1:
        antal_5 = antal_5 + 1
    if antal_5 == 5:
        print ("Yatzy")

antal_6 = 6
for tal in min_lista:
    if tal == 1:
        antal_6 = antal_6 + 1
    if antal_6 == 5:
        print ("Yatzy!")
