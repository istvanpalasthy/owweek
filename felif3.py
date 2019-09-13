n = int(input("Please give a number: "))
paros = 0
paratlan = 0
for i in range(1, n+1):
    print(input("Number:"))
    if (i % 2) == 0:
        print ("Even")
        paros += 1
    else:
        paratlan += 1
        print ("Odd")

        print (paratlan)
        print(paros)
