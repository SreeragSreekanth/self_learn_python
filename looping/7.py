"""Count the number of digits in a number using a while loop."""
n = int(input("Enter the number:"))
cnt = 0
num = n
while n!=0:
    cnt += 1
    n //= 10
print(f"number of digits in {num} is {cnt}")
