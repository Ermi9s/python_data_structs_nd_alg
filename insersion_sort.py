def ins_sort(lst):
    for i in range(1,len(lst)):
        temp = lst[i]
        j = i - 1

        while temp < lst[j] and j >=0:
            lst[j+1] = lst[j]
            lst[j] = temp
            j =-1
    
    return lst

demo = input().split(" ")
demo = [int(i) for i in demo]

print(ins_sort(demo))