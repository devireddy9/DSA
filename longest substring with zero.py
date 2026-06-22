def longest(arr):
    maxlength = 0
    sumindex = {}
    s = 0
    for i, value in enumerate(arr):
        s+=value
        if s==0:
            maxlength = i+1
        elif s in sumindex:
            maxlength = max(maxlength,i-sumindex[s])
        else:
            sumindex[s] = i
    return maxlength
arr = [9, -3, 3, -1, 6, -5]
print(longest(arr))