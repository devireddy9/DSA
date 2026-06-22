def pattern16(n):
    num =65
    for i in range (1, n+1):
        char = chr(num)
        print (i * char,end="")
        num= num+1
        print()



pattern16(5)