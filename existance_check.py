#existance checking 
truth = False
print ("enter trial number")
trnum = int(input())
while (trnum > 0):
    print("enter a list")
    nums = input()
    nums.split()
    
    numlist = [int(x) for x in nums]

    print (numlist)
    
    print("enter a number u r looking for")
    lnumber = int(input())

    for i in numlist:
        if i == lnumber:
            truth = True
            break
        else:
            truth = False
    trnum = trnum - 1

    if truth == True:
        print ("present")
    else:
        print ("not present")
    

    
    


        


