"""Print only prime numbers from 1 to 50 using loops."""

for i in range(2,51):
    flag = True
    for j in range(2,int(i**0.5)+1):
        if i%j == 0:
            flag = False
            break
    if flag:
        print(i,end=" ")