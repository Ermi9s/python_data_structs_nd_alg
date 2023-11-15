sln = []
n = int(input())
m = input().split(" ")
m = [int(i) for i in m]

m.sort()
for i in range(len(m)):
    if m[i] > m[0] and m[i] < m[(len(m) - 1)]:
        sln.append(i)

print(len(sln))

    




