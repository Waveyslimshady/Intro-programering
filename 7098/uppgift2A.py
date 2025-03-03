mening = input ("Skriv en mening eller text för att krypera meingen eller texten.")
output = ""
for bokstav in mening:
    tal= ord (bokstav)

    tal = tal + 2
    chr (tal)
    output = output + (chr(tal))
print (output)