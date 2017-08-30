# 1. Implement a **recursive** function sum_list that takes a
# list of numbers and returns the sum of all the numbers in the list.

def sum_list(list):
        if len(list) == 0:
                sum = 0
                return sum
        if len(list) == 1:
                sum = list[0]
                return sum
        else:
                sum = list[-1]
                newlist = list[:len(list)-1]
                return sum + sum_list(newlist)

# // Test cases:
print "sum_list() tests:"
print sum_list([1, 2, 3, 0, 4, 5])
# 15

print sum_list([])
# 0

print sum_list([-7, 10])
# 3





# 2. Implement a **recursive **function reverse_list that takes a list 
# and returns a list with the elements in the reverse order.

# def reverse_list(list):
#         reversed = []
#         if len(list) == 0:
#                 reversed = []
#                 return reversed
#         if len(list) == 1:
#                 reversed.append(list[-1])
#                 return reversed
#         else:
#                 reversed.append(list[-1])
#                 print reversed
#                 return reverse_list(list[:len(list)-1])

def reverse_list(list):

        if len(list) == 0:
                return list
        if len(list) == 1:
                return list
        else:
                return [list[-1]] + reverse_list(list[:len(list) - 1])


# // Test cases:
print "reverse list tests"
print reverse_list([1, 2, 3, 0, 4, 5])
# [5, 4, 0, 3, 2, 1]

print reverse_list([])
# []

print reverse_list([-7, 10])
# [10, -7]






# 3. Implement a **recursive **function sum_deep that takes an arbitrarily
#  nested list-of-lists and returns the sum of all the numbers contained within
#   the list-of-lists.

# // Paste your code here:

# // Test cases:
# >>> sum_deep([1, 2, 3, 0, 4, 5])
# 15

# >>> sum_deep([1, 2, [3, 0], 4, [[[5], 0]], [[]]])
# 15

# >>> sum_deep([])
# 0

# >>> sum_deep([[], [], [0], [[]]])
# 0

# >>> sum_deep([-7, [10]])
# 3






# 4. Implement a **recursive** function deep_inc that takes an takes 
# an arbitrarily nested list-of-lists and returns an arbitrarily
#  nested list-of-lists with all of the numbers in the original list incremented by one.


#def deep_inc(input):
       # if type(input) is list:


# // Test cases:
# >>> deep_inc([1, 2, 3, 0, 4, 5])
# [2, 3, 4, 1, 5, 6]

#deep_inc([1, 2, [3, 0], 4, [[[5], 0]], [[]]])
# [2, 3, [4, 1], 5, [[[6], 1]], [[]]]

# >>> deep_inc([])
# []

# >>> deep_inc([[], [], [0], [[]]])
# [[], [], [1], [[]]]

# >>> deep_inc([-7, [10]])
# [-6, [11]]






# 5. Implement a **recursive **function flatten_deep that takes an arbitrarily
#  nested list-of-lists and returns a single list with all of the numbers 
#  within the original list-of-lists.

# // Paste your code here:

# // Test cases:
# >>> flatten_deep([1, 2, 3, 0, 4, 5])
# [1, 2, 3, 0, 4, 5]

# >>> flatten_deep([1, 2, [3, 0], 4, [[[5], 0]], [[]]])
# [1, 2, 3, 0, 4, 5, 0]

# >>> flatten_deep([])
# []

# >>> flatten_deep([[], [], [0], [[]]])
# [0]

# >>> flatten_deep([-7, [10]])
# [-7, 10]






# 6. In this exercise, we're going to implement a simple programming language. 
# This programming language is a calculator that will take a number or 
# nested list-of-lists and computes a value based on a series of rules. 
# You'll implement support for numbers, addition, and multiplication. 

# // Paste your code here:

# // Test cases:

# // Numbers evaluate to themselves
# >>> calculator_eval(5)
# 5

# // A list with "+" as the first element returns the sum of the results obtained by
# // evaluating the remaining elements.
# >>> calculator_eval(["+", 1, 2])
# 3

# >>> calculator_eval(["+", 1, ["+", 2, 4]])
# 7

# // "+" with 1 subsequent element returns the result of evaluating that element
# >>> calculator_eval(["+", ["+", 3, 4]])
# 7

# // "+" with no remaining elements returns the additive identity, 0
# >>> calculator_eval(["+"])
# 0

# // "*" Returns the product
# >>> calculator_eval(["*", 10, 10])
# 100

# >>> calculator_eval(["*", 10 ["+", 4, 6]])
# 100

# // "*" with 1 subsequent element returns the result of evaluating that element
# >>> calculator_eval(["*", ["+", 10, 4]])
# 14

# >>> calculator_eval(["*", 23])
# 23

# >>> calculator_eval(["+", ["+", ["+", 23]], 0, 0])
# 23


