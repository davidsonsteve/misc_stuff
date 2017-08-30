#Problem Set #4: Challenge


'''
1. Implement a function, my_range, that takes a positive integer n and returns
an increasing list of all non-negative integers less than n.

// Paste your code here:
'''

def my_range(n):
        output=[]
        i = 0
        while i < n:
                output.append(i)
                i += 1
        return output



#Test cases:
print my_range(5)
#[0, 1, 2, 3, 4]

print my_range(10)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print my_range(1)
# [0]

print my_range(2)
# [0, 1]

print my_range(0)
#[]

'''
2. Implement a function, my_reverse, that takes a list of values and returns a
list with all of the values in the reverse order.

**Each test case must complete in less than 5 seconds.** 

// Paste your code here:
'''
'''
def my_reverse(list):
        output = []
        i = len(list)-1
        while i > -1:
                output.append(list[i])
                i -= 1
        return output
        

'''
'''
#Test cases:
print my_reverse(["a", "b", "c"])
#["c", "b", "a"]

print my_reverse(["a"])
#["a"]

print my_reverse(["b", "a"])
#["a", "b"]

print my_reverse([])
#[]

print my_reverse(my_range(20000))
#[19999, 19998, ... 1, 0]


3. Implement a function, merge_fast, that takes two **_sorted_** (ascending)
lists of numbers and returns a **_sorted_** list (ascending) with all of the
numbers from each the two input lists. (You should not use any sort functions
in your solution)

**Each test case must complete in less than 5 seconds.** (Hint: how can you
take advantage of the fact that the input lists are already sorted?)

'''
'''
def my_range(n):
        output=[]
        i = 0
        while i < n:
                output.append(i)
                i += 1
        return output

'''
def merge_fast(list1, list2):     
        merged = []
        while len(list1)>0 and len(list2)>0:
                if list1[0] <= list2[0]:
                        merged.append(list1[0])
                        list1.pop(0)
                elif list1[0] >= list2[0]:
                        merged.append(list2[0])
                        list2.pop(0)
        if len(list1) == 0:
                for i in list2:
                        merged.append(i)
        if len(list2) == 0:
                for i in list1:
                        merged.append(i)
        return merged
        


'''
merge_fast([1, 2], [3, 4])
#[1, 2, 3, 4]

merge_fast([1, 4], [2, 3])
#[1, 2, 3, 4]

merge_fast([], [1, 2, 3])
#[1, 2, 3]

merge_fast([1, 2, 3], [])
#[1, 2, 3]

merge_fast([5], [0])
#[0, 5]

merge_fast([1, 2, 3], [1, 2, 3])
#[1, 1, 2, 2, 3, 3]

merge_fast([1, 3, 5], [2, 4, 6, 10, 15])
#[1, 2, 3, 4, 5, 6, 10, 15]

merge_fast(my_range(1000), my_range(1000))
#[0, 0, 1, 1, 2, 2, ... 999, 999]

merge_fast(my_range(5000), my_range(5000))
#[0, 0, 1, 1, 2, 2, ... 4999, 4999]
'''
#merge_fast(my_range(10000), my_range(10000))
#[0, 0, 1, 1, 2, 2, ... 9999, 9999]
'''
merge_fast(my_range(20000), my_range(20000))
#[0, 0, 1, 1, 2, 2, ... 19999, 19999]

'''
