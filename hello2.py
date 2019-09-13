#1. Almát szeretnénk vásárolni. Írjunk egy programot, amely billentyűzetről kérje be először azt, hogy
#mennyibe kerül egy kilogramm alma, majd azt hogy hány kilogramm almát szeretnénk venni. A program
#számolja ki, hogy ennyi almáért hány koronát fogunk fizetni.
how_much_a_kilo = int(input ("How much is a 1kg apple?" ))
how_many = int(input ("How many apples?" ))
price = how_much_a_kilo *how_many
print(price)