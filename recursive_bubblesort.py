def recursive_bubblesort(arr,n):
    if n <=1 : return

    for j in range (0 , n-1 ):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]

    recursive_bubblesort(arr,n-1)
    return arr
arr = [2,34,1,42,346,12,4123,123,13,-2]

print(recursive_bubblesort(arr,len(arr) ))