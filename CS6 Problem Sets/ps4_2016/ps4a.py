# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    
    if len(sequence) == 0:
        return []
    if len(sequence) == 1:
        return [sequence]
    else:
        result = []
        for i in range(len(sequence)):
            x = sequence[i]
            rest = sequence[:i] + sequence[i+1:]
            for j in get_permutations(rest):
                result.append(x+j)
        return result


'''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    #pass #delete this line and replace with your code here

#if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

#pass #delete this line and replace with your code here

##example_input = 'abc'
##print('Input:', example_input)
##print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
##print('Actual Output:', get_permutations(example_input))
##
##example_input2 = 'ab'
##print('Input:', example_input)
##print('Expected Output:', ['ab', 'ba'])
##print('Actual Output:', get_permutations(example_input2))
##
##
##example_input3 = '123'
##print('Input:', example_input)
##print('Expected Output:', ['123', '132', '213', '231', '312', '321'])
##print('Actual Output:', get_permutations(example_input3))
