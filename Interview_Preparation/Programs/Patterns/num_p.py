# REVERSE PYRAMID IN NUMBERS
"""
1  
2 1
3 2 1
4 3 2 1
5 4 3 2 1

"""
for i in range(1,6):

    for j in range(i, 0, -1):

        print(j, end=" ")

    print(" ")


n = 5
for i in range(n+1):
    for j in range(1,i+1):
        print(j, end=' ')
    print()

"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

#right
num = 5
for i in range(num):
    for j in range(1, num - i):
        print(" ", end="")
    for k in range(1, i + 2):
        print(k, end="")
    print()

#num triangle
#right
n = 5
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    for k in range(2 * i + 1):
        print(k + 1, end='')
    print()

""" 1
   123
  12345
 1234567
123456789

"""