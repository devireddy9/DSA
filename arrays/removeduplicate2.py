#optimal way to remove duplicate from sorted array

def duplicate(arr):
    n = len(arr)
    i = 0
    for j in range(1,n):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]


    return arr[:i+1]


arr = [0,0,1,1,1,2,2,3,3,4]
print(duplicate(arr))
