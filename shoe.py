t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    s = [(s[i], i+1) for i in range(n)]
    s.sort()
    p = [0]*n
    j = 0
    for i in range(1, n):
        if s[i][0] != s[i-1][0]:
            p[s[j][1]-1] = s[i][1]
            j = i
    if p[s[j][1]-1] == 0:
        print(-1)
        continue
    for i in range(j):
        p[s[i][1]-1] = s[(i+j+1)%n][1]
    print(' '.join(map(str, p)))