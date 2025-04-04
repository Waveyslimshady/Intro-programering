def kelvintocelcius(kelvin):
    return kelvin - 273.15

def celciustofarenhight (celcius):
    return (9/5) * celcius + 32.0

def farenhighttocelcius (farenhight):
    return (5/9) * (farenhight - 32)

def kelvintofarenhight(kelvin):
    c = kelvintocelcius(kelvin)
    f = celciustofarenhight(c)
    return f
temp = float(input("Ange temperatur i grader kelvin: "))
print("Temperaturen är", kelvintofarenhight(temp), "farenhight")