#optimal way
def pair(arr,target):
    for i in range(len(arr)):
        required = target - arr[i]
        if required in arr:
            return [required,arr[i]]
    return "NO"

arr= [2,6,5,8,11]
target = 14
print(pair(arr,target))

def pair2(arr,target):
    seen={}
    for index,num in enumerate(arr):
        required = target - num
        if required in seen:
            return [num,required]
        seen[num]=index
    return [-1,-1]

arr= [2,6,5,8,11]
target = 14
print(pair2(arr,target))