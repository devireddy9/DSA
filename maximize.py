#maximise the count of consecutive

def maximum(arr,num):
    count = 0
    maxcount = 0
    for i in range (len(arr)):
        if arr[i] == num:
            count +=1
            if count > maxcount:
                maxcount = count
        else:
            count = 0
    return maxcount

arr = [1,1,0,1, 0, 1, 0,1,0, 1]
print(maximum(arr,1))