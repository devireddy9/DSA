def pattern15(n):
    num =65
    for i in range (1, n+1):
        for j in range (n-i+1,0,-1):
            char = chr(num)
            print (char,end="")
            num = num + 1
        num = 65
        print()



pattern15(5)