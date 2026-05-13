def insertion_sort(arr):
    n = len(arr)
    for i in range (1,n):
        element = arr[i]
        j =i-1
        while j>=0 and arr[j]>element:
            arr[j+1] =arr[j]
            j-=1
        arr[j+1] = element
    return arr
print (insertion_sort([22,342,2312,1,354,2,2,3423,5412,3,213,3,421,3,-12 ,0,-13]))

