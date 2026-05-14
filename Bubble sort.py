# Brute Force
#in bubble sort the comparision is between adjcent elements
def bubble_sort(arr):
    n = len (arr)
    for i in range (n):
        for j in range(0,n-i-1): #here last element is already sorted
            if arr[j]> arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

print(bubble_sort([1,4,2,45,64,34,2542,1,-12,0]))
