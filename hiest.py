n = int(input())
arr = input().split(" ")
arr = [int(i) for i in arr]
min_index = min(arr)
max_index = max(arr)

total_keyboards = max_index - min_index + 1
stlnky = total_keyboards - n

print(stlnky)