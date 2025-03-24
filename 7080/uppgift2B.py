def farenhighttocelcius (farenhight):
    return (5/9) * (farenhight - 32)
temp = float(input("Ange temperatur i grader farenhight: "))
print("Temperaturen är", farenhighttocelcius (temp), "celcius")