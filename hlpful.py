arr = input().split('+')
arr = [int(i) for i in arr]
arr.sort()

for i in range(len(arr)):
    if i != (len(arr) - 1):
      print(arr[i] , end= '+')
    elif i == (len(arr) - 1):
       print(arr[i])

