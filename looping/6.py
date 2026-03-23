"""Stop printing numbers when a negative number appears (break). Example list: [2, 4, -3, 5]."""

lst = list(map(int,input("enter the list:").split()))

for num in lst:
    if num < 0:
        break
    print(num,end=" ")