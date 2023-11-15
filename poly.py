m = int(input())
sln =[]
for case in range(m):
    n = int(input())
    lst = input()
    for i in range(n-1):
        if lst[i+1:].count(lst[i]) >= 1:
            sln.append("NO")
        else:
            sln.append("YES")
for j in sln:
    print(j)