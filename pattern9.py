def pattern9 (n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end="")
        for k in range (2* i + 1):
           print("*", end="")
        print()
    for i in range (n):
        print(i * " ", end="")
        print ((2*(n-i)-1)*"*")



pattern9(4)