def maximum(arr):
    maxsum = float('-inf')
    for i in range (len(arr)):
        currentsum = 0
        for j in range (i+1,len(arr)):
            maxsum = max(maxsum,currentsum+arr[j])
    return maxsum

arr = [-2, -1, -7, -2, 0, -4]
print(maximum(arr))