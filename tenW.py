t = int(input().strip())
rslt = []
for _ in range(t):
    n = int(input())
    st = []
    for i in range(n):
        a, b = map(int, input().strip().split())
        st.append((a, b, i+1))
    st.sort()
    max_quality = -1
    count = -1
    for a, b, i in st:
        if a <= 10 and b > max_quality:
            max_quality = b
            count = i
    rslt.append(count)

for i in rslt:
    print(i)