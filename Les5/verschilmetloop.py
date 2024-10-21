import random

aantal_oef = int(input("Aantal oefeningen ?"))
i = 0

while i < aantal_oef:
    getal_1 = random.randint(1,20)
    getal_2 = random.randint(1,20)

    if getal_1 < getal_2:
    #old_getal1 = getal_1
    #getal_1 = getal_2
    #getal_2 = old_getal1
        getal_1, getal_2 = getal_2, getal_1

    print("Geef het verschil tussen " + str(getal_1) + " en " + str(getal_2))
    result = int(input())

    while result != getal_1 - getal_2:
        print("Fout antwoord")
        print("Geef het verschil tussen " + str(getal_1) + " en " + str(getal_2))
        result = int(input())

    print("Juist antwoord")

#print(result == getal_1 - getal_2)