#optimal way
def basichashing2(arr):
    countdict ={}
    for i in arr:
        if i in countdict:
            countdict[i] +=1
        else:
            countdict[i] =1
    for key,value in countdict.items():
        print(f"{key} : {value}")


basichashing2([1,2,2,3,42,45,2,4,2,1,4,52,6,3])