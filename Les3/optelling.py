import random

getal_1 = random.randint(1,20)
getal_2 = random.randint(1,20)

print("Geef de som van " + str(getal_1) + " en " + str(getal_2))
result = int(input())

#print(result)
#print(getal_1 + getal_2)

if result == getal_1 + getal_2:
    print("juist")
else:
    print("fout")

print(result == getal_1 + getal_2)