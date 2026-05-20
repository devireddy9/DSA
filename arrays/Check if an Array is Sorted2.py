#optimal way to find array is already sorted or not

def arraysort(arr):
    for i in range (1 ,len(arr)):
        for j in range (i-1):
            if arr[i] < arr[j]:
                return "FALSE"
    return "TRUE"

arr = [1,2,3,4,5,6,7,8,9]
print(arraysort(arr))