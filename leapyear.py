year = int(input("Enter year: "))
leap_year = year % 4

if (year %400 == 0) or (year %100 != 0) and (year % 4==0):
    print("It is leap year")
else:
    print("It is not leap year")
    
