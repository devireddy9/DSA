#optimal way

def longest(arr,k):
    n = len(arr)
    maxlength = 0
    right = 0
    left = 0
    sum = arr[0]
    while right<n:
        while left<=right and sum>k:
            sum-=arr[left]
            left+=1
        if sum ==k:
            maxlength = max(maxlength, right-left+1)
        right+=1
        if right < n:
            sum+=arr[right]
    return maxlength
nums = [10, 5, 2, 7, 1, 9]
print(longest(nums,15 ))