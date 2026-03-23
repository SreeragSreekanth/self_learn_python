"""Find the sum of all even Fibonacci numbers less than n."""

num = int(input("Enter the number of series:"))
a,b = 0,1
total_even = 0
while b < num:
    if b%2 == 0:
        total_even += b
    a,b = b,a+b
print(total_even)