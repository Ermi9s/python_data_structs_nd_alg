m = int(input())
rank = 1
ulst = []

for i in range (m):
    lst = input().split(" ")
    lst = [int(i) for i in lst]
    ulst.append(lst)

for i in range (len(ulst)):
    if sum(ulst[i]) > sum(ulst[0]):
        rank +=1

print(rank)
