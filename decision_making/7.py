"""7. Leap Year Checker
Check whether a year is a leap year."""
year = int(input())

if year%400 == 0 or (year%100 != 0 and year%4 == 0):
    print("Leap year")
else:
    print("Not Leap Year")