k = input().split(' ')
k = [int(i) for i in k]
m,n = k
frst = []
scnd = []
for i in range (n):
    frst.append("#")
for i in range(n-1):
    scnd.append(".")
scnd.append("#")

trd = scnd.reverse()
al = True
for i in range(m):
    if i % 2 == 0:
        for j in frst:
            print(j,end="")
        print('')
    elif i%2 !=0 and al:
        for j in scnd:
            print(j,end="")
            al = False
        print('')
    elif i%2 !=0 and al == False:
        for j in trd:
            print(j,end="")
            al = True
        print('')

    


         

