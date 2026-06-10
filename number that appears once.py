def occur(arr):
    count = 0
    for i in range (len(arr)):
        num = arr[i]
        for j in range (len(arr)):
            if arr[j] == num:
                count +=1

            if count == 1:
                return num
    return -1
arr = [4,1,2,1,2]
print(occur(arr))
