# collections.Counter()
# A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.

#Sample Code

"""
    >>> from collections import Counter
    >>> 
    >>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
    >>> print Counter(myList)
    Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
    >>>
    >>> print Counter(myList).items()
    [(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
    >>> 
    >>> print Counter(myList).keys()
    [1, 2, 3, 4, 5]
    >>> 
    >>> print Counter(myList).values()
    [3, 4, 4, 2, 1]
"""
# Task
"""
    Raghu is a shoe shop owner. His shop has "X" number of shoes.
    He has a list containing the size of each shoe he has in his shop.
    There are "N" number of customers who are willing to pay "xi" amount of money only if they get the shoe of their desired size.
"""
# Your task is to compute how much money Raghu earned.

# Input Format
"""
    The first line contains "X", the number of shoes.
    The second line contains the space separated list of all the shoe sizes in the shop.
    The third line contains "N", the number of customers.
    The next "N" lines contain the space separated values of the "shoe size" desired by the customer and "xi", the price of the shoe.
"""

# Constraints
"""
    0 < X < 10^3
    0 < N <= 10^3
    20 < xi < 100
    2 < shoe size < 20
"""
# Output Format

# Print the amount of money earned by Raghu.

# Code from Here
from collections import Counter

X = int(input())
size_list = map(int, input().split())
N = int(input())
# L = map(tuple,(map(int,input().split()) for _ in range(N)))

size_order = list()
x = list()
for i in range(N):
    a = tuple(map(int, input().split()))
    size_order.append(a[0])
    x.append(a[-1])

n = Counter(size_list)

total = 0
for i in range(len(size_order)):
    ord = size_order[i]
    if ord in n.keys():
        if n[ord] > 0:
            total += x[i]
            # print(f"\nAdding amount: {x[i]}, total: {total}")
            n[ord] -= 1

print(total)