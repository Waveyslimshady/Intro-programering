nummer = input ("Ge mig ett tal mellan 0 till 1000.")
nummer = int (nummer)
print(nummer)
if nummer >=0 and nummer <=9:
    print ("ensiffrigt tal")
elif nummer >=9 and nummer <=99:
    print ("tvåsiffrigt tal")
elif nummer >=100 and nummer <=999:
    print ("tresiffrigt tal")
elif nummer >=1000 and nummer <=9999:
    print ("Är minst fyrsiffriga tal.")
elif nummer <=0:
    print ("Tal mindre än 0 är negativa.")