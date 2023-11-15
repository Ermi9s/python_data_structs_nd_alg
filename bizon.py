cups = input().split(" ")
cups = [int(i) for i in cups]
medals = input().split(" ")
medals = [int(i) for i in medals] 
n = int(input())
if sum(cups) > 0: reqc = 1
else: reqc = 0
if sum(medals) > 0: reqm = 1 
else: reqm = 0

c = sum(cups)
m = sum(medals)

while c > 5:
    reqc +=1
    c -= 5

while m > 10:
    reqm +=1
    m -= 10

if reqc + reqm <= n:
    print("YES")
else:
    print("NO")
    