wiek = 19
kasa = 40

if wiek >= 18:
    if kasa >= 35:
        print("Możesz wejść:")

if wiek >=18 and kasa >= 35:
    print("Możesz wejść")

if wiek <= 12 or kasa >= 30:
    print("Możesz wejść")

if not wiek > 12 or kasa >= 30:
    print("Możesz wejść")
else:
    print("Nie możesz wejść")

if True or False and False:
    print("Prawda")
else:
    print("Fałsz")