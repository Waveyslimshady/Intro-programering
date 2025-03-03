mening = input ("Mata in en krypterad mening eller text.")
output = ""
for bokstav in mening:
    tal= ord (bokstav)

    tal = tal - 2
    chr (tal)
    output = output + (chr(tal))
print (output)