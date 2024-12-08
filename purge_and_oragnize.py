# '''
# Given a list of numbers, write a function that returns a list that...
#     Has all duplicate elements removed.
#     Is sorted from least to greatest value.

# Examples
# unique_sort([1, 2, 4, 3]) ➞ [1, 2, 3, 4]
# unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]) ➞ [1, 2, 3, 4]
# unique_sort([6, 7, 3, 2, 1]) ➞ [1, 2, 3, 6, 7]
# '''

def unique_sort(lst):
    no_dubs = []
    for i in lst:
        if i not in no_dubs:
            no_dubs.append(i)
    for i in range(len(no_dubs)-1):
        swap = False
        for j in range(len(no_dubs)-1-i):
            if no_dubs[j] > no_dubs[1 + j]:
                no_dubs[j],no_dubs[1 + j] = no_dubs[1 + j],no_dubs[j]
                swap = True
        if not swap:
            break
    return no_dubs


# print(unique_sort([1, 2, 4, 3]))
# print(unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]))
# print(unique_sort([6, 7, 3, 2, 1]))

from sorting_alg import bubble_sort_2

def unique_sort_2(lst):
    no_dubs = []
    for i in lst:
        if i not in no_dubs:
            no_dubs.append(i)
    return bubble_sort_2(no_dubs)


print(unique_sort_2([6, 7, 3, 2, 1]))