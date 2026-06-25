def max(arr):
    count = 0
    element = 0
    for num in arr:
        if count == 0:
            count +=1
            element = num
        elif element == num:
            count +=1
        else:
            count-=1
    realcount = arr.count(element)
    if realcount>=len(arr)/2:
        return element," occured ",realcount, "times"
    return "None"

arr = [2, 2, 1, 1, 1, 2, 2]
print(max(arr))