#optimal way

def rotate(arr,k):
    n = len (arr)
    if n == 0: return
    if k > n: k = k-n
    start =0
    end = n-1
    while start < end:
        arr[start],arr[end] = arr[end],arr[start]
        start +=1
        end-=1
    return arr

arr = [1, 2, 3, 4, 5]
print(rotate(arr, 2))