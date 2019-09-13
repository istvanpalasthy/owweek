T = int(input("Please give a number between 1800 and 2099: "))
a = T%19
b = T%4
c = T%7
d = (19*a+24)%30
e = (2*b+4*c+6*d+5)%7 
While: T <= 1799 or T >= 3000
print("Invalid number!")
if e == 6 and d == 29:
       H == 50
elif e == 6 and d == 28:
        H == 49
else:
      H = 22 + d + e
      if H <= 31:
        print("Marcius.", H)
      elif H:
       print("Aprilis.",H-31)