import datetime

print("Enter two dates and i will find the number of days between them.")
print("---------------- Date 1 ----------------\n")
year1 = int(input('Enter a year: '))
month1 = int(input('Enter a month: '))
day1 = int(input('Enter a day: '))
date1 = datetime.date(year1, month1, day1)

print("---------------- Date 2 ----------------\n")

year2 = int(input('Enter a year: '))
month2 = int(input('Enter a month: '))
day2 = int(input('Enter a day: '))
date2 = datetime.date(year2, month2, day2)

print(f"\nYour two dates are {date1-date2} away from each other")