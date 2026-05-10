#This is the better approch than brute force
def reversearray(array):
    p1, p2 = 0, len(array) - 1
    while p1< p2:
        array[p1],array[p2] = array[p2],array[p1]
        p1 += 1
        p2 -= 1
    print(array)
reversearray([1,2,3,4,5,6,7,8,9])