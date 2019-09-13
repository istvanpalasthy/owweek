s = input("give a name:")
for i in s:
    if i == " ":
        i = s.replace(i, "")
    print(i)