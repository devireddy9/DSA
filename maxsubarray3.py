def maximum(arr):
    maxi = float('-inf')
    sum =0
    for i in range (len(arr)):
        sum += arr[i]
        if sum >0:
            maxi =sum
        else:
            sum = 0
    return (max(maxi,sum))

arr = [-2, -1, -7, -2, -10, -4]
print(maximum(arr))