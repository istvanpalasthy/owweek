a = int(input("stars? "))
for i in range(a):
    ws = ' ' * (a - i - 1)
    st = '*' * i
    print(ws + st + '*' + st + ws)