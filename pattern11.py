def pattern11(n):
    for i in range(1,n+1):
        val = 1 if i%2 !=0 else 0
        for j in range (i):
            print(val,end="")
            val = 1 - val
        print()



pattern11(4)