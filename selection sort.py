#this will select the small number and swap the number
def SelectionSort(arr):
    n = len(arr)
    for i in range (n):
        min_index = i
        for j in range (i+1,n):
            if  arr[j] <arr[min_index] :
                arr[min_index], arr[j] = arr[j],arr[min_index]

    return arr
print(SelectionSort([1,3,5,2,-1,-5,0,6,8,4,9]))
