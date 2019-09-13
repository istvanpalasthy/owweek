a = int(input("Please give a number: "))
b = int(input("Please give a number: "))
c = int(input("Please give a number: "))
if a**2 + b**2 == c**2 or b**2 + c**2== a**2 or a**2 + c**2 == b**2:
    print("Megfelel")
else:
    print("Nem felel")