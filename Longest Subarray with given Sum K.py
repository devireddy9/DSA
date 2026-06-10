def substring(arr,k):
    n = len(arr)
    maxlength = 0
    for startindex in range (n):
        for endindex in range (startindex,n):
            sum = 0
            for i in range (startindex, endindex+1):
                sum +=  arr[i]
            if sum == k:
                maxlength = max(maxlength,endindex-startindex+1)

    return (maxlength)




arr = [10, 5, 2, 7, 1, 9]
print(substring(arr,15))