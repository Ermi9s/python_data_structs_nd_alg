def digit_adder (number):
    if number <= 9:
        return number
    return digit_adder(number % 10) + int(digit_adder(number/10))
print("enter a number")
num = int(input())

print(digit_adder(num))