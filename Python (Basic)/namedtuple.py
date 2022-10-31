### NAMED TUPLES ###


# Basically, namedtuples are easy to create, lightweight object types.
# They turn tuples into convenient containers for simple tasks.
# With namedtuples, you don’t have to use integer indices for accessing members of a tuple.

# Example

# Code 01
"""
    >>> from collections import namedtuple
    >>> Point = namedtuple('Point','x,y')
    >>> pt1 = Point(1,2)
    >>> pt2 = Point(3,4)
    >>> dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
    >>> print dot_product
    11
"""

# Code 02
"""
    >>> from collections import namedtuple
    >>> Car = namedtuple('Car','Price Mileage Colour Class')
    >>> xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
    >>> print xyz
    Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
    >>> print xyz.Class
    Y
"""

# Task

# Dr. John Wesley has a spreadsheet containing a list of student's "IDs", "marks", "class" and "name".
# Your task is to help Dr. Wesley calculate the average marks of the students.

# Note:
"""
    1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet.
    2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won't change.)
"""

# Input Format
"""
    The first line contains an integer N, the total number of students.
    The second line contains the names of the columns in any order.
    The next N lines contains the "IDs", "marks", "class" and "marks", under their respective column names.
"""

# Constraints

# 0 < N <= 100

# Output Format

# Print the average marks of the list corrected to 2 decimal places.


##################################################
################ SOLUTION HERE ###################
##################################################

from collections import namedtuple

n = int(input())

entry = list()
for i in range(n+1):
    if i == 0:
        header = input()
        students = namedtuple("students", header)
    else:
        student = input().split()
        entry.append(students(student[0], student[1], 
                     student[2], student[3]))

sum = 0
for ele in entry:
    sum += int(ele.MARKS)
    
print(sum/n)
