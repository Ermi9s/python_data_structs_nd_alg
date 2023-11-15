def selection_sort(lst):
    for i in range(0,len(lst)-1):
        min_index = i
        for j in range(i+1,len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        
        if i != min_index:
            temp = lst[i]
            lst[i] = lst[min_index]
            lst[min_index] = temp
    
    return lst

demo = input().split(" ")
demo = [int(i) for i in demo]

print(selection_sort(demo))