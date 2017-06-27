"""

>>> shrink('1235')
2

>>> shrink('13')
4

>>> shrink('1123581321')
9

"""


def shrink(numbers):
    sum_numbers = sum([int(x) for x in numbers])
    if sum_numbers >= 10:
        doubles = str(sum_numbers)
        sum_doubles = sum([int(x) for x in doubles])
        print(sum_doubles)
    else:
        print(sum_numbers)

    
