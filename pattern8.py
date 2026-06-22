def pattern8(n):
    for i in range (n):
        print(i * " ", end="")
        print ( (2*(n-i)-1) * "*")


pattern8(4)