#linear searxh

def linearsearch(arr,element):
    for i in range (len(arr)):
        if arr[i] == element:
            return (f"Element {element} is in {i} index")
    return (f"Element {element} not found")

arr = [1,2,3,4,5,6,7,7,9]
print(linearsearch(arr,9))