n = int(input())
snl = []
for _ in range(n):
    cd = list(map(int, input().split()))
    st = list(input())
    num = 0
    i = 0
    while i < cd[0]:
        if st[i] == 'B':
            j = min(i + cd[1], cd[0])
            if 'B' in st[i:j]:
                num += 1
            i = j
        else:
            i += 1
    snl.append(num)

for num in snl:
    print(num)
    

