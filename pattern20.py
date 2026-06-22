'''
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
'''

def pattern20(n):
    for i in range(1,n+1):
        stars = "*"*i
        spaces = 2*(n-i)*" "
        print(stars+spaces+stars)
    for j in range(n-1,-1,-1):
        stars = "*"*j
        spaces = 2*(n-j)*" "
        print(stars+spaces+stars)


pattern20(5)