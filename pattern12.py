def pattern12(n):
    for i in range (1,n+1):
        for j in range (1,i+1):
            print(j,end="")
        space = 2*(n-i)
        for j in range (space):
            print(" ",end="")
        for l in range (i,0,-1):
            print(l,end="")

        print()


pattern12(5)