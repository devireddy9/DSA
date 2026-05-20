# optimal way
def large(arr):
    n = len(arr)
    if n == 0 or n==1:
        return(arr[-1],arr[-1])
    small,nextsmall,large,nextlarge = float('inf'),float('inf'),float('-inf'),float('-inf')
    for i in range (n):
        small = min(small,arr[i])
        large =max(large,arr[i])
    for i in range (n):
        if arr[i] < nextsmall and arr[i] != small:
            nextsmall =arr[i]
        if arr[i] > nextlarge and arr[i]!= large:
            nextlarge = arr[i]
    return (small, nextsmall, large,nextlarge)

print(large([1, 2, 4, 6, 7, 5] ))