#NUMBER LISTS! 


'''
1. Implement a function, count_even that takes a list of numbers and returns
    the number of even numbers in the list.

// Paste your code here:
'''

def count_even(list):
    count = 0
    for i in list:
        if i%2 == 0:
            count += 1
    return count

'''

#Test cases:
count_even([])
#0

count_even([0, 1, 2])
#2

count_even([-2, 0, 2, 4])
#4

count_even([3, 5, 7, 17])
#0

count_even([2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
#10

2. Implement a function, sum_list, that takes a list of numbers and returns the sum of the numbers in the list.

// Paste your code here:
'''

def sum_list(list):
    sum = 0
    for i in list:
        sum = sum + i
    return sum


'''
// Test cases:
>>> sum_list([5, 6, 7])
18

>>> sum_list([])
0

>>> sum_list([1, 8, 12, -21])
0

>>> sum_list([1])
1

>>> sum_list([7, 7, 7, 7, 7, 7, 7, 7])
56




3. Implement a function, first_odd, that takes a list of numbers and returns the first odd number in the list. If there are no odd numbers in the list, return None.

// Paste your code here:
'''

def first_odd(list):

    firstodd = None
    for i in list:
        if i%2 != 0:
            firstodd = i
            return firstodd
    return firstodd





'''
// Test cases:
>>> first_odd(0, [1])
1

>>> first_odd(0, [4, 3])
3

>>> first_odd(0, [4, 3, 2])
3

>>> first_odd(0, [])
None

>>> first_odd(0, [1, 2, 3])
1

>>> first_odd(0, [2, 4, 6, 8, 10, 11])
11

>>> first_odd(0, [6, 8, 2])
None




4. Implement a function, max_list, that takes a list of numbers and returns
the largest number in the list. If there are no numbers in the list, return None.

// Paste your code here:
'''

def max_list(list):

    max = "None"

    if len(list) > 0:
        max = list[0]
        for i in list:
            if i > max:
                max = i
    return max


'''
// Test cases:
>>> max_list([])
None

>>> max_list([-1, -2, -3, -4, -5])
-1

>>> max_list([2, 1, 3])
3

>>> max_list([1, 1, 0, 0, 0, 7])
7

>>> max_list([-3, -5, -7, 3, 6, 5])
6

>>> max_list([10, 0, 0])
10




5. Implement a function, nth_even, that takes 2 parameters, a number (e.g. n)
and a list, and returns n'th even number in the list. If there is no n'th even
number, returns None.

Note that, per programming convention, n = 0 means the first even number.

// Paste your code here:
'''

def nth_even(n, list):

    nthEven = "None"
    evens = []
    for i in list:
        if i%2 == 0:
            evens.append(i)
    if n >= len(evens):
        return nthEven
    return evens[n]


'''
// Test cases:
>>> nth_even(0, [2])
2

>>> nth_even(0, [1, 2, 3])
2

>>> nth_even(1, [1, 2, 4, 3])
4

>>> nth_even(1, [5, 2, 3, 4, 1])
4

>>> nth_even(3, [9, 2, 3, 7, 7, 4, 5, 6, 7, 8, 9])
8

>>> nth_even(0, [])
None

>>> nth_even(3, [])
None

>>> nth_even(1, [3, 1, 2])
None

>>> nth_even(6, [1, 2, 3, 4, 5, 6])
None


'''


