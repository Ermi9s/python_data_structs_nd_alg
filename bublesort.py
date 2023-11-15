def buble_sort(lst):
    for i in range(len(lst)-1,0,-1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    
    return lst

demo = input().split(" ")
demo = [int(i) for i in demo]

print(buble_sort(demo))

