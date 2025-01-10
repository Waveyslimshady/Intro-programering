Spela = "J"
while Spela == "J":
    nummer = input ("Gissa ett nummer mellan 1 till tio!")
    nummer = int (nummer)
    if nummer == 4:
            print ("rätt")
    else:
        print ("Du gissade fel")
    Spela = input ("Vill du spela igen? J/N")
