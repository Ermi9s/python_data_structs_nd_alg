t = int(input())
results = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if sum(a) % n == 0:
        results.append('YES')
    else:
        results.append('NO')

for result in results:
    print(result)