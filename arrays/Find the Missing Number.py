#Given an array arr[] of size n-1 with distinct integers in the range of [1, n]

def missing(arr):
    n = len(arr) +1
    for i in range (1, n+1):
        found = False
        for j in range (n-1):
            if arr[j] == i:
                found = True
                break
        if not found:
            return i
    return -1

arr = [8, 2, 4, 5, 3, 7, 1]
print(missing(arr))