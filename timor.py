m = int(input())
sln=[]
for case in range(m):
    n = int(input())
    bit = input()
    bit.split()
    bit = [int(i) for i in bit]
    if n > 3:
          for i in range(len(bit)):
            if bit[i] == bit[(-1-i)]:
                 break
            else:
                bit.pop(0+i)
                bit.pop((-1-i))
    elif n == 3:
        if bit[0] != bit[2]:
            bit.pop(0)
            bit.pop(-1)
        else:
            sln.extend(bit)
    elif n == 2:
        if bit[0] != bit[-1]:
            bit.pop(0)
            bit.pop(1) 
        
    sln.append(len(bit))
for j in sln:
    print(j)
              

