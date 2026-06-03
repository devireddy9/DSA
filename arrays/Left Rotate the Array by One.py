##brute force to rotate element

def rotate(arr):
    n = len(arr)
    rotatedarr = []
    for i in range (1,n):
        element = arr[i]
        rotatedarr.append(element)

    rotatedarr.append(arr[0])
    return rotatedarr
arr = [0,1,2,3,4]
print(rotate(arr))

def rotate2(arr):
    n = len(arr)
    newarr = [0]*n

    for i in range(1,n):
        newarr[i-1] = arr[i]
    newarr[n-1] = arr[0]
    return newarr
arr = [0,1,2,3,4]
print(rotate2(arr))