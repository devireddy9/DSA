#optimal way

def union(arr1, arr2):
    n = len(arr1)
    m = len (arr2)
    sorted=[]
    i,j = 0,0

    while (i <n and j<m):
        if arr1[i] < arr2[j]:
            if not sorted or sorted[-1] != arr1[i]:
                sorted.append(arr1[i])
            i+=1
        elif arr1[i] > arr2[j]:
            if not  sorted or sorted[-1] != arr2[j]:
                sorted.append(arr2[j])
            j+=1
        else:
            if not sorted or sorted[-1] != arr1[i]:
                sorted.append(arr2[j])
            i+=1
            j+=1
    while i < n:
        if not sorted or sorted[-1] != arr1[i]:
            sorted.append(arr1[i])
        i+=1
    while j < m:
        if not union or sorted[-1] != arr2[j]:
            sorted.append(arr2[j])
        j+=1

    return sorted

arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]
print(union(arr1,arr2))