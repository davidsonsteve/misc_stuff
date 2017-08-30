#NUMBERS!



def add(a, b, c):
    sum = a + b + c
    return sum



def average_3(a, b, c):
    average = (a+b+c) / 3.0
    return average



def min_3(a,b,c):
    min = a
    if (b < min) :
        min = b
    if (c < min) :
        min = c
    return min


def max_3(a,b,c):
    max = a
    if (b > max) :
        max = b
    if (c > max) :
        max = c
    return max


def median_3(a,b,c):

    if b <= a <= c or c<=a<=b:
        return a
    if a <= b <= c or c<=b<=a:
        return b
    if b <= c <= a or a<=c<=b:
        return c

    
'''
def median_3(a,b,c):
    input = [a,b,c]
    med = 0
    min = min_3(a,b,c)
    
    max = max_3(a,b,c)
    
    for i in input:
        if input.count(i)>1:
            med = i
        if i != min and i != max:
            med = i
            

    return med
'''

        
