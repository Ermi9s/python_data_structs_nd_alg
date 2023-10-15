#factorial using recursion
def factorial(num):
    if num == 1 or num == 0:
        return 1
    return num * factorial(num - 1)

print("Enter a number\n")
number = int(input())
fact = factorial(number)

print(fact)
