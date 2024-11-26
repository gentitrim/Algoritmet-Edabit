'''Create a function that takes a list of numbers or strings and returns a list with the items from the original list stored into sublists. Items of the same value should be in the same sublist.
Examples

advanced_sort([2, 1, 2, 1]) ➞ [[2, 2], [1, 1]]'''


def advanced_sort(lst):
    result = []
    
    for i in lst:
        elem = []
        for j in range(lst.count(i)):
            elem.append(i)
        if elem not in result:
            result.append(elem)

    return result

print(advanced_sort([2, 1, 2, 1,4,3,4]))
print(advanced_sort(["b", "a", "b", "a", "c"]))