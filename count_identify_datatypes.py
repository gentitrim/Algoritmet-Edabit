"""
Given a function that accepts unlimited arguments, check and count how many data types are in those arguments. Finally return the total in a list.
List order is:
[int, str, bool, list, tuple, dictionary]
Examples
count_datatypes(1, 45, "Hi", False) ➞ [2, 1, 1, 0, 0, 0]
"""

def count_datatypes(*args):
    data_types = {"int":0, "str":0, "bool":0, "list":0, "tuple":0, "dict":0}
    for j in args:
        # print(str(type(j))[8:-2])
        data_types[str(type(j))[8:-2]] +=1
    return list(data_types.values())

print(count_datatypes())
print(count_datatypes(1, 45, "Hi", False))
print(count_datatypes("Nice", "Bad", 1, 999, 0, False, {"Hi": "Bye"}))  #[3, 2, 1, 0, 0, 1])