def mergesort(arr):
    mid = len(arr) // 2
    if len(arr) ==1: return arr
    return merge(mergesort(arr[:mid]), mergesort(arr[mid:]))

def merge(left, right):
    result=[]
    i = j  = 0
    while i < len(left) and j< len(right):
        if left[i] < right[j]:
            result.append(left[i]); i+=1
        else:
            result.append(right[j]); j+=1
    result.extend(left[i:] or right[j:])
    return result


print(mergesort([1,2,5,2,3,7,2,1,345,7,221,2,214,88]))