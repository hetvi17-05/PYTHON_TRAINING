# Inverted Pyramid of Numbers.
rows = 5

a = 0

for i in range(rows, 0, -1):

    a +=1

    for j in range(1, i + 1):

        print(a, end="")

    print("")

"""
11111
2222
333
44
5
"""

"""
rows = 5
a = 0
for num in range(rows,0,-1):
    a+=1
    for j in range(num):
        print(num,end=" ")
    print()
    
------> output:-
5 5 5 5 5 
4 4 4 4
3 3 3
2 2
1
    """
