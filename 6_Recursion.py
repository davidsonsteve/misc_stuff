# 1. Implement a **recursive** function sum_list that takes a
# list of numbers and returns the sum of all the numbers in the list.
import math

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
# print "sum_list() tests:"
# print sum_list([1, 2, 3, 0, 4, 5])
# # 15
#
# print sum_list([])
# # 0
#
# print sum_list([-7, 10])
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
# print "reverse_list() tests"
# print reverse_list([1, 2, 3, 0, 4, 5])
# # [5, 4, 0, 3, 2, 1]
#
# print reverse_list([])
# # []
#
# print reverse_list([-7, 10])
# [10, -7]






# 3. Implement a **recursive **function sum_deep that takes an arbitrarily
#  nested list-of-lists and returns the sum of all the numbers contained within
#   the list-of-lists.



##def sum_deep(lst):
##        if len(lst) == 0:
##                return 0
##        if len(lst) == 1:
##                if type(lst[0]) is list:
##                        return sum_deep(lst[0])
##                else:
##                        return lst[0]
##        else:
##                if type(lst[0]) is list:
##                        return sum_deep(lst[0])
##                else:
##                        return lst[0] + sum_deep(lst[1:])

def sum_deep(lst):
        sum = 0
        for i in lst:
                if type(i) is list:
                        sum += sum_deep(i)
                else:
                        sum += i
        return sum

 # // Test cases:
#print "sum_deep() tests:"
#print sum_deep([1, 2, 3, 0, 4, 5])
 # 15

#print sum_deep([1, 2, [3, 0], 4, [[[5], 0]], [[]]])
 # 15

#print sum_deep([])
 # 0

#print sum_deep([[], [], [0], [[]]])
 # 0

#print sum_deep([-7, [10]])
 #3






# 4. Implement a **recursive** function deep_inc that takes an takes 
# an arbitrarily nested list-of-lists and returns an arbitrarily
#  nested list-of-lists with all of the numbers in the original list incremented by one.


def deep_inc(lst):
        newlst = []
        for i in lst:
                if type(i) is list:
                        newlst.append(deep_inc(i))
                else:
                        newlst.append(i+1)
        return newlst


# // Test cases:
#print "deep_inc() tests:"
#print deep_inc([1, 2, 3, 0, 4, 5])
# [2, 3, 4, 1, 5, 6]

#print deep_inc([1, 2, [3, 0], 4, [[[5], 0]], [[]]])
# [2, 3, [4, 1], 5, [[[6], 1]], [[]]]

#print deep_inc([])
# []

#print deep_inc([[], [], [0], [[]]])
# [[], [], [1], [[]]]

#print deep_inc([-7, [10]])
# [-6, [11]]






# 5. Implement a **recursive **function flatten_deep that takes an arbitrarily
#  nested list-of-lists and returns a single list with all of the numbers 
#  within the original list-of-lists.

# // Paste your code here:

def flatten_deep(lst):
        newlst = []
        for i in lst:
                if type(i) is list:
                        newlst.extend(flatten_deep(i))
                else:
                        newlst.append(i)
        return newlst

# // Test cases:
#print "flatten_deep() tests:"
#print flatten_deep([1, 2, 3, 0, 4, 5])
#[1, 2, 3, 0, 4, 5]

#print flatten_deep([1, 2, [3, 0], 4, [[[5], 0]], [[]]])
#[1, 2, 3, 0, 4, 5, 0]

#print flatten_deep([])
#[]

#print flatten_deep([[], [], [0], [[]]])
#[0]

#print flatten_deep([-7, [10]])
#[-7, 10]






# 6. In this exercise, we're going to implement a simple programming language. 
# This programming language is a calculator that will take a number or 
# nested list-of-lists and computes a value based on a series of rules. 
# You'll implement support for numbers, addition, and multiplication. 

# // Paste your code here:

##def calculator_eval(input):
##        if type(input) is int:
##                return input
##        if type(input[0]) is str:
##                answer = 0
##                for i in input[1:]:
##                        if input[0] == "+":
##                                answer += calculator_eval(i)
##                        elif input[0] == "*":
##                                answer = answer * calculator_eval(i)
##        return answer
                
def calculator_eval(input):
        if type(input) is int:
                return input
        if type(input[0]) is str:
                answer = 0
                for i in input[1:]:
                        if input[0] == "+":
                                answer += calculator_eval(i)
                        if input[0] == "*":
                                if answer == 0:
                                        answer += 1
                                
                                answer = answer * calculator_eval(i)
        return  answer



# // Test cases
print "Test Cases: calculator_eval()"
# // Numbers evaluate to themselves
print calculator_eval(5)
# 5

# // A list with "+" as the first element returns the sum of the results obtained by
# // evaluating the remaining elements.
print calculator_eval(["+", 1, 2])
# 3

print calculator_eval(["+", 1, ["+", 2, 4]])
# 7

# // "+" with 1 subsequent element returns the result of evaluating that element
print calculator_eval(["+", ["+", 3, 4]])
# 7

# // "+" with no remaining elements returns the additive identity, 0
print calculator_eval(["+"])
# 0

# // "*" Returns the product
print calculator_eval(["*", 10, 10])
# 100

print calculator_eval(["*", 10, ["+", 4, 6]])
# 100

# // "*" with 1 subsequent element returns the result of evaluating that element
print calculator_eval(["*", ["+", 10, 4]])
# 14

print calculator_eval(["*", 23])
# 23

print calculator_eval(["+", ["+", ["+", 23]], 0, 0])
# 23
