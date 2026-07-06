#bruteforce
def maximum(arr):
    maxi = float('-inf')
    startindex = 0
    endindex = 0
    for i in range (len(arr)):
        for j in range (i,len(arr)):
            sum = 0
            for k in range (i,j+1):
                sum += arr[k]
                if sum > maxi:
                    if maxi in arr:
                        maxi = sum
                        for m in range (len(arr)):
                            index = []
                            if arr[m]== maxi:
                                index.append(m)
                        return maxi," indexs are ",index
                    else:
                        max=sum
                        startindex = i
                        endindex = j
    return maxi," indexs are ",startindex,endindex

arr = [-2, -11, -7, -2, -10, -4]
print(maximum(arr))
