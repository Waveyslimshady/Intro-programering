ord = input ("Skriv in ett ord.")

vokaler = "aeiouyåäö"
konsonanter = "BbCcDdFfGgHhKjKkLlMmNnPpQqRrSsTtVvXxZz"
output = ""

for bokstav in ord:
    output = output + bokstav
    if bokstav in konsonanter:
        output = output + "o"
        output = output + bokstav

print (output)