#brute force zeros to end

def zeros(arr):
    temp = [0] * len(arr)
    index = 0
    for num in arr:
        if num !=0:
            temp[index] = num
            index+=1
    for i in range(len(arr)):
        arr[i] =temp[i]

    return arr

arr = [0,2,3,4,0,34,9,0,34,9,0]
print(zeros(arr))