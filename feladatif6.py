n = int(input("How many numbers do ya want chap?: "))
list = []
for i in range(1,n+1):
    a = int(input("Number: "))
    list.append(a)
print("Smallest: ", min(list))
print("Largest: ", max(list))