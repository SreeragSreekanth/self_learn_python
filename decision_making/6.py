"""6. Simple Calculator
Take two numbers and an operator (+, -, *, /) and perform the operation."""

num1 = int(input())
num2 = int(input())
op = input()

if op =="+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
else:
    print(num1/num2)