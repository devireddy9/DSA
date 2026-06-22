'''
Given an integer n, write a function to print all numbers from 1 to n (inclusive) using recursion.

You must not use any loops such as for, while, or do-while.
The function should print each number on a separate line, in increasing order from 1 to n.

Example 1

Input: n = 5

Output:
1

2

3

4

5
'''
def recursion(n):
    if n == 0:
        return
    # print(n) === gives reverse order because it was not saved in stack
    recursion(n - 1)
    print(n) # saved in stack and prints after if condition satisfies
recursion(5)