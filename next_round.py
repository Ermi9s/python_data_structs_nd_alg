sln = []
x = input()
x.split()
lst = [int(x[0]),int(x[2])]

y = input()
y.split(" ")

lsty=[ i for i in y]
for i in lsty:
    if i == " ":
        lsty.remove(i)
print(lsty)
lsty =[int(i) for i in lsty]

for i in lsty[:lst[0]]:
    if i > lst[1]:
        sln.append(i)
       
print(sln)
print(len(sln))