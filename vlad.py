n = int(input())
m = input().split(" ")
m = [int(i) for i in m]

sln = set()

for i in range(n):
    if m[(n-1)-i] not in sln:
        sln.add(m[(n-1)-i])
        ans = m[(n-1)-i]

print(ans)

