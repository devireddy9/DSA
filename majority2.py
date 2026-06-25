def max(arr):
    dict = {}
    for num in arr:
        if num in dict:
            dict[num]+=1
        else:
            dict[num]=1
    for num,count in dict.items():
        if count >= len(arr)/2:
            return num," repeated ",count, " times."

arr = [2, 2, 1, 1, 1, 2, 2]
print(max(arr))