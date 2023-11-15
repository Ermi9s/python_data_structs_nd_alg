n = int(input())
wrd = input()

l = [i for i in wrd]
for i in range(1, n+1):
    if n % i == 0:
        l[:i] = l[i-1::-1]

for i in l:
    print(i, end="")




