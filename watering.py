n = input().split(" ")
n = [float(i) for i in n]

m = input().split(' ')
m = [float(i) for i in m]
sum = sum(m)
count = 0
target = m[0]
if n[2] < n[1]:
    for j in range(int(n[0] -1)):
        if ((n[1] * target)/sum) < n[2]:
            r= max(m[1:])
            m.pop(m.index(r))
            sum = sum - r
            count +=1

else:
    count = len(m) - 1

print(count)

