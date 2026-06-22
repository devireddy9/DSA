def max (arr):
    length = len(arr)
    count = 0
    for i in range(length):
        for j in range(i,length):
            if arr[j] == arr[i]:
                count+=1
        if count >= length/2:
            return arr[i] ," occured ",count,"times"

arr= [7, 0, 0, 1, 7, 7, 2, 7, 7]
print(max(arr))