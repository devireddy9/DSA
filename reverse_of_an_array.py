#brute force

def reverse_of_an_array(array):
    length = len(array)
    reversedarray = []
    for i in range (length-1,-1,-1):
        reversedarray.append(array[i])
    print (reversedarray)

reverse_of_an_array([1,2,3,4,5,6,7,8,9])