n = int(input())
lst = []
for i in range(n):
    lst.append(input())

lst = [f"{i[0]}{len(i) - 2}{i[-1]}" if len(i) > 10 else i for i in lst] 

for i in lst:
    print(i)


