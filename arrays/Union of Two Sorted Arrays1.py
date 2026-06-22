def union(arr1,arr2):
    freq = {}
    for i in range (len(arr1)):
        freq[arr1[i]] = freq.get(arr1[i],0)+1

    for i in range (len(arr2)):
        freq[arr2[1]] = freq.get(arr2[i],0)+1

    union = sorted(freq.keys())
    return union

arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]
print(union(arr1,arr2))