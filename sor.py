n = int(input())
a = list(map(int, input().split()))
b = a[::-1].index(max(a))
c = a[-b-1:] + a[:-b-1]
if c == sorted(c):
    print(b)
else:
    print(-1)


