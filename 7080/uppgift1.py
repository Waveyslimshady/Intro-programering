def kelvintocelcius(kelvin):
    return kelvin - 273.15
temp = float(input("Ange temperatur i grader Kelvin: "))
print("Temperaturen är", kelvintocelcius(temp), "Celcius")