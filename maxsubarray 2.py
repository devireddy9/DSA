def maximum(arr):
    maxi = float('-inf')
    for i in range (len(arr)):
        for j in range(i,len(arr)):
            sum = 0
            for k in range (i,j+1):
                sum+=arr[k]
                maxi =max(maxi,sum)
    return maxi
arr = [-2, -1, -7, -2, 10, -4]
print(maximum(arr))