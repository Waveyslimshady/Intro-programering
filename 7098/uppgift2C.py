mening = input ("Skriv en mening.")


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
