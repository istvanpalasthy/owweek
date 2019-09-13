size = int(input("pleas give me a number: "))
b = (2 * size) -2
for i in range(1, size+1,):
    for j in range(0, b):
     print(end=" ")
    for j in range(0, i + 1):
        print ("*", end= " ")
    print(" ")