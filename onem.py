st = input()
st1 = input()
mv = 0
if len(st) < len(st1):
    temp = st
    ltemp = st1 
else: 
    temp = st1
    ltemp = st

n = 0 
for i in range(len(ltemp)):
    if len(temp) == 1:
        if ltemp[-1 - i] != temp[-1]:
            n = i
            break
    elif ltemp[-1 - i] != temp[-1-i]:
        n = i
        break

print((len(temp)-n)+(len(ltemp)-n))
