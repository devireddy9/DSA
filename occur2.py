#best approct
def occur(arr):
    num = 0
    for i in arr:
        num ^= i
    return num
arr = [0,1,2,1,2]
print(occur(arr))

#this only works when only 1 single element