
def quicksort(arr,low, high):
    if low < high:
        pivot = sort(arr,low,high)
        quicksort(arr,low,pivot-1)
        quicksort(arr,pivot+1,high)


def sort(arr,low,high):
    pivot = arr[high]
    i = low -1
    for j in range (low,high):
        if arr[j] <= arr[high]:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1





arr =[1,23,142,25,23,46,3,412,57,-2,4]
quicksort(arr,0,len(arr)-1)
print(arr)

