"""Check if a number is a palindrome using a loop."""
num = int(input("Enter the number:"))
n = num
rev = 0

while n!= 0:
    dig = n%10
    rev = dig + rev*10
    n //= 10

if num == rev:
    print("palindrome")
else:
    print("Not Palindrome")