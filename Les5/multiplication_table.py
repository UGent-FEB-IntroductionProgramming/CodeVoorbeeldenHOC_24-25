print("Multiplication Table")

for i in range(1, 10):
    print(i, end=" ")
print("")
print("-------------------")
for j in range(1, 10):
    print(j,"|", end=" ")
    for k in range(1, 10):
        print(k*j, end=" ")
    print()
