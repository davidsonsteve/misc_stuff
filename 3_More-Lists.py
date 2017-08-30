#Problem Set #3: More Lists
'''
1. Implement a function, two_list_nth, that takes two lists of values and returns the 
n'th item as if the two sequences were concatenated together.

// Paste your code here:
'''

def two_list_nth(n, list1, list2):
        newList = []
        for i in list1:
                newList.append(i)
        for i in list2:
                newList.append(i)
        if len(newList) > n:
                print newList[n]
        else:
                print "None"
        
'''
#Test cases:
print(two_list_nth(0, [], ["steve"]))
#"steve"

print(two_list_nth(0, ["zeke"], ["steve"]))
#"zeke"

print(two_list_nth(1, ["zeke"], ["steve"]))
#"steve"

two_list_nth(1, ["zeke", "butters"], ["steve"])
#"butters"

two_list_nth(2, ["zeke", "butters"], ["steve"])
#"steve"

two_list_nth(2, ["zeke", "butters"], ["merlin", "steve"])
#"merlin"

two_list_nth(3, ["zeke", "butters"], ["merlin", "steve"])
#"steve"

two_list_nth(3, ["zeke", "butters", "merlin", "steve"], [])
#"steve"

two_list_nth(4, ["zeke", "butters", "merlin", "steve"], [])
#None

two_list_nth(10, ["zeke", "butters", "merlin", "steve"], [])
#None

two_list_nth(2, ["zeke", "butters"], [])
#None

two_list_nth(0, [], [])
#None


2. Implement a function, even_concat, that takes two lists of numbers and
returns a list with all of the even numbers in each of the lists
(in the same order they appeared in the original two lists).

// Paste your code here:
'''

def even_concat(list1, list2):
        newList = []
        for i in list1:
                if i%2 == 0 or i == 0:
                        newList.append(i)
        for i in list2:
                if i%2 == 0 or i ==0:
                        newList.append(i)
        print newList

'''                
Test cases:
>>> even_concat([1, 2], [3, 4])
[2, 4]

>>> even_concat([1, 3], [5, 7])
[]

>>> even_concat([4, 2], [0, 6])
[4, 2, 0, 6]

>>> even_concat([4, 2], [])
[4, 2]

>>> even_concat([5], [0, 6])
[0, 6]

>>> even_concat([], [0, 6])
[0, 6]

>>> even_concat([1, 7, -6, 3], [9, 7, 1])
[-6]


3. Implement a function, sum_lists, that takes a list of list of numbers and
returns the sum of all the numbers in the inner lists.

// Paste your code here:
'''

def sum_lists(list):
        sum = 0
        for i in list:
                for j in i:
                     sum += j
        return sum

'''
// Test cases:
>>> sum_lists([])
0

>>> sum_lists([[1], [2]])
3

>>> sum_lists([[1, 2]])
3

>>> sum_lists([[1], [2], [3]])
6

>>> sum_lists([[1], [], [], [1]])
2

>>> sum_lists([[], [], [], []])
0

>>> sum_lists([[], [5], [], [1, 2, 3, 4]])
15

>>> sum_lists([[1, 2], [5], [8, -10], [1, 2, 3, 4]])
16



4. Implement a function, partition, that takes a list of numbers and a number (n), and returns a list of two lists. The first list contains all the numbers less than n, while the second list contains all the numbers greater than or equal to n. The numbers within each list should appear in the same order they appeared in the original list.

// Paste your code here:
'''

def partition(n, list):
        lessThan = []
        greaterThan = []
        
        output = [lessThan, greaterThan]
        for i in list:
                if i < n:
                        lessThan.append(i)
                else:
                        greaterThan.append(i)
        print output


'''
// Test cases:
>>> partition(3, [1, 2, 4, 5])
[[1, 2], [4, 5]]

>>> partition(3, [1, 2, 4, 3, 5, 0])
[[1, 2, 0], [4, 3, 5]]

>>> partition(3, [2, 1])
[[2, 1], []]

>>> partition(0, [2, 1])
[[], [2, 1]]

>>> partition(1, [2, 1])
[[], [2, 1]]

>>> partition(12, [])
[[], []]

>>> partition(10, [15, -1, -5, 20])
[[-1, -5], [15, 20]]


5. Implement a function, merge, that takes two **_sorted_** (ascending) lists of numbers and returns a **_sorted_** list (ascending) with all of the numbers from each the two input lists. (You should not use any sort functions in your solution)

// Paste your code here:
'''

def merge(list1, list2):
        joined = []
        output  = []
        for i in list1:
                joined.append(i)
        for i in list2:
                joined.append(i)
        while len(joined)>0:
                least = min(joined)
                output.append(least)
                idx = joined.index(least)
                del joined[idx]
        print output




'''
// Test cases:
>>> merge([1, 2], [3, 4])
[1, 2, 3, 4]

>>> merge([1, 4], [2, 3])
[1, 2, 3, 4]

>>> merge([1, 4], [1, 2, 3])
[1, 1, 2, 3, 4]

>>> merge([], [1, 2, 3])
[1, 2, 3]

>>> merge([], [])
[]

>>> merge([1, 2, 3], [])
[1, 2, 3]

>>> merge([5], [0])
[0, 5]

>>> merge([1, 2, 3], [1, 2, 3])
[1, 1, 2, 2, 3, 3]

>>> merge([1, 3, 5], [2, 4, 6, 10, 15])
[1, 2, 3, 4, 5, 6, 10, 15]
'''

