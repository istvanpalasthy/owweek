a = str(input("Please enter a sentence: "))
b = 0
for i in a:
    if b == 0: 
        if i == "<":
            b += 1
        else:
            continue
    else:
        if  i == ">":
            b -= 1
        else:
            print(i)