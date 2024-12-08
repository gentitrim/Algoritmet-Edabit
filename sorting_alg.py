#bubble sort
lst = [8, 3, 5, 20, 7]
def bubble_sort(lst):
    for i in range(len(lst)-1):
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                lst[i] , lst[i + 1] = lst[i + 1] , lst[i]
    return lst

# print(bubble_sort(lst))


# bubble sort v2

def bubble_sort_2(lst):
    for j in range(len(lst) - 1):
        swap = False
        for i in range(len(lst) - 1 - j):
            if lst[i + 1] < lst[i]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swap = True
        if not swap:
            break

    return lst



#