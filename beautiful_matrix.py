raw=[]

for i in range(5):
    col=input().split(" ")
    raw.append(col)

for i in raw:
    for j in i:
        if j == "1":
            print(abs((raw.index(i) + 1) - 3) + abs((i.index(j) + 1)-3) )


