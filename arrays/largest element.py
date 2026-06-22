# optimal way to find largest element

def largest (arr):
    largestnumber = 0
    for i in range (len(arr)):
        if arr[i] >=largestnumber:
            largestnumber = arr[i]
    return largestnumber
arr = [0,-3,-23,-12354,-86,-98765,99]
print(largest(arr))