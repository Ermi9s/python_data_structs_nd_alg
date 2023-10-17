prob = int(input())
lst = []
sln=0
for n in range(prob):
    lst.append(input())


for i in lst:
    list(i)
    if i.count("1") >= 2:
        sln += 1

print(sln)

    
    