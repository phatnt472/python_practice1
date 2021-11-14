month = int(input("Enter a month: "))
year = int(input("Enter a year: "))

isLeapYear = False
if year > 0:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
      print(f'{year} is leap year!')
      isLeapYear = True
    else:
       print(f'{year} is not leap year!')
else:
    isLeapYear = False
    print("Year is wrong!")
if 1 <= month <= 12:
    if month == 2:
        if isLeapYear:
            print(f'{month} has 29 days!')
        else:
            print(f'{month} has 28 days')
    elif month in [4,6,9,11]:
        print(f'{month} has 30 days!')
    else:
        print(f'{month} has 31 days!') 
else:
    print("Month is wrong!")