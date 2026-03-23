"""Reverse a number. Example: input 1234 → output 4321."""

num = int(input("Enter a number:"))
rev = 0
n = num

while n!=0:
    dig = n%10
    rev = dig + rev*10
    n //= 10

print(f"reverse of {num} is {rev}")