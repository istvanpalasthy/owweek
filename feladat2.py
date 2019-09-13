
give_hour1 = int(input("Give me the first hour:"))*3600
give_minute1 = int(input("Give me the first minute:"))*60
give_second1 = int(input("Give me the first second:"))


give_hour2 = int(input("Give me the second hour:"))*3600
give_minute2 = int(input("Give me the second minute:"))*60
give_second2 = int(input("Give me the second second:"))
result = (give_hour1 + give_minute1 + give_second1)-(give_hour2 + give_minute2 + give_second2)

print(result)
