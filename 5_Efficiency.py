
def my_range(n):
        output=[]
        i = 0
        while i < n:
                output.append(i)
                i += 1
        return output


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
def merge_even_faster(list1, list2):
        merged=[]
        
        while len(list1)>0 and len(list2)>0:
                
                if list1[0]<list2[0]:
                        merged.append(list1[0])
                        list1.pop(0)
                elif list1[0]>list2[0]:
                        merged.append(list2[0])
                        list2.pop(0)
                elif list1[0] == list2[0]:
                        merged.append(list1[0])
                        list1.pop(0)
        if len(list1)==0:
                merged.extend(list2)
        if len(list2)==0:
                merged.extend(list1)
        
        return merged
'''


def merge_faster(list1, list2):
        merged=[]
        i = 0
        j = 0
        while i <= len(list1) and j <= len(list2):
                if i == len(list1):
                        merged.extend(list2[j:])
                        return merged
                if j == len(list2):
                        merged.extend(list1[i:])
                        return merged
                if list1[i] <= list2[j]:
                        merged.append(list1[i])
                        i += 1
                else:
                        merged.append(list2[j])
                        j += 1
        return merged        

merge_faster([1, 2], [3, 4])
#[1, 2, 3, 4]

merge_faster([1, 4], [2, 3])
#[1, 2, 3, 4]

merge_faster([], [1, 2, 3])
#[1, 2, 3]

merge_faster([1, 2, 3], [])
#[1, 2, 3]

merge_faster([5], [0])
#[0, 5]

merge_faster([1, 2, 3], [1, 2, 3])
#[1, 1, 2, 2, 3, 3]

merge_faster([1, 3, 5], [2, 4, 6, 10, 15])
#[1, 2, 3, 4, 5, 6, 10, 15]
'''
merge_fast(my_range(1000), my_range(1000))

merge_faster(my_range(1000), my_range(1000))
#[0, 0, 1, 1, 2, 2, ... 999, 999]

merge_faster(my_range(5000), my_range(5000))
#[0, 0, 1, 1, 2, 2, ... 4999, 4999]

#merge_faster(my_range(10000), my_range(10000))
#[0, 0, 1, 1, 2, 2, ... 9999, 9999]

merge_faster(my_range(20000), my_range(20000))
#[0, 0, 1, 1, 2, 2, ... 19999, 19999]
'''

