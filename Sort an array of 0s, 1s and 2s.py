def sort(arr):
    count0=count1=count2 =0
    for num in (arr):
        if num == 0:
           count0+=1
        elif num ==1:
           count1 +=1
        else:
            count2+=1
        index = 0
    for i in range (count0):
        arr[index]=0
        index+=1
    for i in range (count1):
        arr[index]=1
        index+=1
    for i in range (count2):
        arr[index]=2
        index+=1
    return arr



arr = [1, 0, 2, 1, 0]
print(sort(arr))