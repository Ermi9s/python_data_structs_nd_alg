n = int(input())
sln = [[]*n]
for _ in range(n):
    ln = int(input())
    if ln%2 == 0: n = int(ln/2)
    if ln%2 != 0: n = int(ln/2) + 1
    st = input().split(" ")
    sln1 = []
    for i in range(n):
        sln1.append(st[i])
        sln1.append(st[-1 - i])
    if len(sln1) > ln:
        sln1.pop(-1)
    sln.append(sln1)

for i in sln:
    for j in i:
        print(j,end =" ")
    print("")


