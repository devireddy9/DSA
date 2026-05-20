#bruteforce to remove duplicates

def duplicate(arr):
    noduplicate=[]
    for i in range (len(arr)):
        if arr[i] in noduplicate:continue
        noduplicate.append(arr[i])

    return noduplicate
arr = [0,0,1,1,1,2,2,3,3,4]
print(duplicate(arr))
