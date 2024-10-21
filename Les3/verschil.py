import random

from Les3.if_demo import getal

getal_1 = random.randint(1,20)
getal_2 = random.randint(1,20)

if getal_1 < getal_2:
    #old_getal1 = getal_1
    #getal_1 = getal_2
    #getal_2 = old_getal1
    getal_1, getal_2 = getal_2, getal_1

print("Geef het verschil tussen " + str(getal_1) + " en " + str(getal_2))
result = int(input())

#print(result)
#print(getal_1 + getal_2)

if result == getal_1 - getal_2:
    print("juist")
else:
    print("fout")

print(result == getal_1 - getal_2)