def seven_boom(lst):
    for i in lst:
        if "7" in str(i):
            return "Boom!"
    return "there is no 7 in the list"

print(seven_boom([1, 2, 3, 4, 5, 6, 7]))
print(seven_boom([8, 6, 33, 100]))
