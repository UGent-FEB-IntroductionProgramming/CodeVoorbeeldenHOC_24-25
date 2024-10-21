import random

getal = random.randint(1,100)

gok = int(input("Guess a number between 1 and 100: "))

while gok != getal:
    if gok > getal:
        print("Too high")
    else:
        print("Too low")
    gok = int(input("Guess number again ? "))


print("Thank you for playing!")