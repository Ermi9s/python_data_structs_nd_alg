import heapq

n = input().split(" ")
n = [float(i) for i in n]

m = input().split(" ")
m = [float(i) for i in m]
count = 0
target = m[0]
m = m[1:]
heapq.heapify(m)
total = sum(m)
length = len(m)

if n[2] < n[1]:
    while ((n[1] * target)/total) < n[2] and m:
        removed = heapq.heappop(m)
        total -= removed
        length -= 1
        count += 1

print(count)