"""Print the multiplication table of a number (input n, table till 10)."""
n = int(input("Enter the number:"))
for i in range(1,11):
    print(f"{i}*{n} = {i*n}")
