def recursive_insertion_sort(arr,n):

    if n<=1: return arr

    recursive_insertion_sort(arr,n-1)
    element = arr[n-1]
    j =n -2
    while j>=0 and arr[j] > element:
        arr[j+1] = arr[j]
        j-=1

    arr[j+1] = element
    return arr
arr =[7,1,9,3,6,-2]
print(recursive_insertion_sort(arr, len(arr)))

