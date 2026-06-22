# optimal way to move zeros to end

def zerosos(arr):
    j = -1
    for i in range (len(arr)):
        if arr[i] == 0:
            j = i
            break
    if j == -1:
        return
    for i in range (j+1 , len(arr)):
        if arr[i] != 0:
            arr[i],arr[j] = arr[j],arr[i]
            j+=1
    return arr

arr = [0,2,3,4,0,34,9,0,34,9,0]
print(zerosos(arr))