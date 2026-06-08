def union (arr1,arr2):
    union = set(arr1) | set(arr2)
    return sorted(union)


arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]
print(union(arr1, arr2))