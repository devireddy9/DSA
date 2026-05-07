def pattern14(n):
    num =65
    for i in range (1, n+1):
        for j in range (1, i+1):
            char = chr(num)
            print (char,end="")
            num +=1
        print()



pattern14(5)