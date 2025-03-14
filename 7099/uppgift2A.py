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
medel = sum (min_lista) / len(min_lista)
print('antal ettor', antal_1) 

