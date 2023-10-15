#power function using recursion
def power (num, pow):
    if pow == 0:
        return 1
    if pow == 1:
       return num
    return num * power(num, pow - 1)

def npower (num, pow):
    if pow == 0:
        return 1
    if pow == - 1:
       return 1/num
    return 1/num * npower(num, pow + 1)

print("enter a number")
number = int(input())
print("Enter the power of the number")
exp = int(input())

if (exp >=0 ):
    print(power(number,exp))
if(exp <= 0):
    print(npower(number,exp))