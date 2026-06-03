# brute force

def rotate (arr,n):
    if n> len(arr): return "Not Possible"

    arr1 = arr[:n]
    arr2 = arr[n:]
    arr2.extend(arr1)
    return arr2

arr = [1,2,3,4,5,6,7]
print(rotate(arr,2))


def rotate2(arr,k):
    n = len(arr)
    if n == 0: return

    if k > n: k = k-n
    temp = arr[-k:]
    for i in range (n-k-1,-1,-1):
        arr[i+k] = arr[i]
    for i in range (k):
        arr[i] = temp[i]
    return arr

arr = [1,2,3,4,5,6,7]
print(rotate2(arr,2))

