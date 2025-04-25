import random 

kortlek = []
j = 2
while j < 11:
    i = 0
    while i < 4:
        kortlek.append(j)
        i = i + 1
    j = j + 1

k = 0    
while k < 12:
    kortlek.append(10)
    k = k + 1
l = 0   
while l < 4:
    kortlek.append(11)
    l = l + 1
l = 0
#----viktig----#
#print(kortlek)
#print("antal 10:", kortlek.count(10))
#print("antal kort i kortlek:", len(kortlek))

random.shuffle (kortlek)
spelarhand = []
dealern = []
dealern.append (kortlek.pop())
print ("dealern:",dealern)
spelarhand.append (kortlek.pop())
spelarhand.append (kortlek.pop())
print ("spelarhand:",spelarhand)
svar_fortsätt = input ("hit eller stand? h/s")
while svar_fortsätt == ("h"):
    spelarhand.append (kortlek.pop())
    print ("spelarhand:", spelarhand)
    print ("dealern:", dealern)
    
    # om tjock svar_fortsätt = "nej"
    if sum (spelarhand) > 21:
        print ("Spelaren är tjock. Dealern vinner!")
        svar_fortsätt = "nej"
    else:
        svar_fortsätt = input ("hit eller stand? h/s")

if sum (spelarhand) <= 21:

    # datorn får kort tills den har minst 16 poäng
    while sum (dealern) < 16:
        dealern.append (kortlek.pop())
        print ("dealern", dealern)
        print ("spelarhand:", spelarhand)
        

# avgör vem som vann
if sum (dealern) > 21 and sum(spelarhand) > 21:
    print ("Både dealern och spelaren har blivit tjocka. Oavgjort!")
elif sum (dealern) > 21:
    print ("Dealern har blivit tjock. Spelaren vinner!")
elif sum (spelarhand) > 21:
    print ("Spelaren har blivit tjock. Dealern vinner!")

# den som har 21 vinner, vid lika blir det oavgjort
else:
    if sum (dealern) == 21 and sum(spelarhand) == 21:
        print ("Både dealern och spelaren har 21. Oavgjort!")
    elif sum (dealern) == 21:
        print ("Dealern har 21. Dealern vinner!")
    elif sum (spelarhand) == 21:
        print ("Spelaren har 21. Spelaren vinner!")
        
# den som är närmast 21 vinner (närmast lägre)
    else:
        if abs (21 - sum(dealern)) < abs(21 - sum(spelarhand)):
            print ("Dealern är närmast 21. Dealern vinner!")
        elif abs (21 - sum(dealern)) > abs(21 - sum(spelarhand)):
            print ("Spelaren är närmast 21. Spelaren vinner!")
        else:
            print ("Både dealern och spelaren är lika nära 21. Oavgjort!")