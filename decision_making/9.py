"""9. Day of the Week
Use match-case to print the day name based on a number (1–7).
"""
day = int(input())
match day:
    case 1:print("Sunday")
    case 2:print("Monday")
    case 3: print("Tuesday")
    case 4:print("Wednesday")
    case 5:print("Thursday")
    case 6:print("Friday")
    case 7:print("Saturday")
    case _:print("Invalid")