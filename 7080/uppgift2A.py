def celciustofarenhight (celcius):
    return (9/5) * celcius + 32.0
temp = float(input("Ange temperatur i grader celcius: "))
print("Temperaturen är", celciustofarenhight (temp), "farenheight")