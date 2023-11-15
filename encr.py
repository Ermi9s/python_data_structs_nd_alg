test = int(input())
result = []
for _ in range(test):
    n = int(input())
    io = input()
    lst = [i for i in io]
    sln = []
    j = 0
    for i in range(1,n):
        if lst[i] == lst[j] and i != j:
            sln.append(lst[i])
            j = i + 1
            continue
    
    result.append(sln)
    
for i in result:
    for j in i:
        print(j,end="")
    print("")









