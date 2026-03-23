"""Print numbers from 1 to 50 skipping multiples of 3 and 5 (continue)."""

for i in range(1,51):
    if i%3==0 or i%5==0:
        continue
    print(i,end=" ")