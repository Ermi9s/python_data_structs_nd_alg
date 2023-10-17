n = int(input())
x = 0

for n in range(n):
    line = input()
    countp = line.count("+")
    countn = line.count("-")

    if countp != 0:
        x+=1
    if countn !=0:
        x-=1


print(x)


