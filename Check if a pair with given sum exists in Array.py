def pair(arr,target):
    n = len(arr)
    for i in range (n):
        for j in range (i+1,n):
            if arr[i] +arr[j] == target:

                return arr[i],arr[j]
    return [-1,-1]
arr= [2,6,5,8,11]
target = 14
print(pair(arr,target))