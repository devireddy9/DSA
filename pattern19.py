def pattern19(n):
    for i in range (n):
        stars = (n-i)*"*"
        spaces = (2*i)*" "
        print(stars+spaces+stars)

    for j in range (n-1,-1,-1):
        stars = (n-j)*"*"
        spaces = (2*j)*" "
        print(stars+spaces+stars)


pattern19(4)