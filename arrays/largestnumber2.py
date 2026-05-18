#bruteforce method

def largest(arr):
    n = len(arr)
    if n==0 or n == 1: return (arr[-1] , arr[-1])

    arr.sort()
    largest = arr[-1]
    smallest = arr[1]
    nextlargest = arr[-2]
    nextsmallest = arr[2]
    return(largest,nextlargest,smallest,nextsmallest)
print(largest([8, 10,100, 5, 7,123,-1,0, 9]))