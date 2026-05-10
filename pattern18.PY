def pattern18(n):
    for i in range (1,n+1):
        char = 65 + (n-i)
        for j in range ( i):
            print(chr(char+j),end="")
        print()

pattern18(4)