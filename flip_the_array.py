'''
Flip the Array

Create a function that flips a horizontal list into a vertical list, and a vertical list into a horizontal list.

In other words, take an 1 x n list (1 row + n columns) and flip it into a n x 1 list (n rows and 1 column), and vice versa.
Examples

flip_list([1, 2, 3, 4]) ➞ [[1], [2], [3], [4]]
# Take a horizontal list and flip it vertical.
# '''

def flip_list(lst):
    for index,i in enumerate(lst):
        if not isinstance(i,list):
            lst[index] = [i]
        else:
            lst[index] = i[0]

    return lst


print(flip_list([1, 2, 3, 4])) #[[1], [2], [3], [4]]
print(flip_list([[5], [6], [9]])) #[5, 6, 9])
print(flip_list([[7], [8], [9],[55]])) #[7, 8, 9, 55])
print(flip_list([7, 8, 9, 55]))  #[[7], [8], [9], [55]])
print(flip_list([[1], [2]])) #[1, 2])
print(flip_list([5, 8])) #[[5], [8]])
print(flip_list([2])) #[[2]])
print(flip_list([])) #[])