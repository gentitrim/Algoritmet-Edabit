'''
Write a function that pairs the first number in an array with the last, the second number with the second to last, etc.
Examples

pairs([1, 2, 3, 4, 5, 6, 7]) ➞ [[1, 7], [2, 6], [3, 5], [4, 4]]
'''



def pairs(lst):
    new_lst = []
    if len(lst)%2 == 0:
        for i in range(int(len(lst)/2)):
            new_lst.append([lst[i], lst[-1-i]])
    else:
        for i in range(int(len(lst)/2) + 1):
            new_lst.append([lst[i], lst[-1-i]])

            
    return new_lst



print(pairs([1, 2, 3, 4, 5, 6, 7])) #[[1, 7], [2, 6], [3, 5], [4, 4]])
print(pairs([1, 2, 3, 4, 5, 6])) #[[1, 6], [2, 5], [3, 4]])
print(pairs([5, 9, 8, 1, 2]))  #[[5, 2], [9, 1], [8, 8]])
print(pairs([1, 1, 4, 4, 5, 5]))  #[[1, 5], [1, 5], [4, 4]])
print(pairs([9, 9, 9, 9, 3, 3, 9]))  #[[9, 9], [9, 3], [9, 3], [9, 9]])
print(pairs([5, 6, 7]))   #[[5, 7], [6, 6]])
print(pairs([5, 6])) #[[5, 6]])
print(pairs([5])) #[[5, 5]])
print(pairs([])) #[])