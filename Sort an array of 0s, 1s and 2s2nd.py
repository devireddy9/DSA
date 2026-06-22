#better approch

def sort (arr):
    count0=count1=count2=0
    for i in arr:
        if i ==0:
            count0+=1
        elif i == 1:
            count1+=1
        else:
            count2+=1
    for i in range(count0):
        arr[i] = 0
    for i in range(count0,count1+count0):
        arr[i]=1
    for i in range (count0+count1,len(arr)):
        arr[i]=2
    return arr
arr =  [0, 2, 1, 2, 0, 1]
print(sort(arr))