#Bruteforce  way to find array is already sorted or not

def arraysorted(arr):
    for i in range(len(arr)):
        for j in range (i+1,len(arr)):
            if arr[i] > arr[j]:
                return "FALSE"

    return "TRUE"

arr = [1,2,3,4,5,6,7,8,9]
print(arraysorted(arr))