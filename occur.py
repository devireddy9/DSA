def occur(arr):
    dict={}
    for i in range(len(arr)):
        count = 1
        if arr[i] not in dict:
            dict[arr[i]] = count
        else:
            dict[arr[i]] +=1
    for num, value in dict.items():
        if value == 1:
            return num
    return -1

arr = [4,1,2,1,2]
print(occur(arr))

#Your code uses O(N) time complexity (which is optimal) but requires O(N) space