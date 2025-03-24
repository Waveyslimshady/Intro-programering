tärningar = [0, 2, 0, 1, 2, 1, 0, 1, 1, 2, 0, 0]

print(tärningar)
for i in range(len(tärningar)):
    if tärningar[i] == 0:
        tärningar[i] = 3 
print(tärningar)