#bruteforce
def largest(arr):
    arr.sort()
    return arr[-2]
print(largest([8, 10, 5, 7, 9]))