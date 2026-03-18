"""10. Menu-Based Program
Display a menu:
1. Add
2. Subtract
3. Multiply
4. Exit
Use match-case to perform the chosen operation."""
num1 = int(input())
num2 = int(input())
op = int(input())

match op:
    case 1:print(num1+num2)
    case 2:print(num1-num2)
    case 3:print(num1*num2)
    case 4:exit()
    case _:print("invalid")