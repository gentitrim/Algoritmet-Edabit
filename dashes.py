# def dashes(n):
#     string = ""
#     for i in range(n):
#         string += "-"
#     return string


# print(dashes(10))

# nr = 10
# for el in range(1, nr+1):
#     print((nr-el) * ' ', end='' )
#     print( el * '* ')
        

# def many_a(num):
#     a = ""
#     for i in range(num):
#         a += "a"
#     return "ed" + a + "bit"

# print(many_a(5))

# def check(*args):
#     for i in args:
#         if i == False:
#             return False
#     return True
        
# print(check(True,False,True))


# def words(s):
#     number_dict = {
#     "one": 1,
#     "two": 2,
#     "three": 3,
#     "four": 4,
#     "five": 5,
#     "six": 6,
#     "seven": 7,
#     "eight": 8,
#     "nine": 9,
#     "zero": 0
# }
#     return number_dict[s]

# print(words("one"))


# def count_letter(letter,word):
#     count = 0
#     for i in word:
#         if i.upper() == letter.upper():
#             count +=1
#     return count

# print(count_letter("a","Albania"))


# a = ["genti","lala","ing"]
# def find_index(lst,s):
#     for i in range(len(lst)):
#         if lst[i] == s:
#             return i
        
# print(find_index(a,"ing"))

# lista = ["beni","tomka","tretr"]
# def forbidden(lst,letter):
#     for i in range(len(lst)):
#         if letter in lst[i]:
#             return True
#     return False

# print(forbidden(lista,"r"))


# def add_index(lst):
#     for i in range(len(lst)):
#         lst[i]+=i
#     return lst

# lista  = [3,5,6,7]

# print(add_index(lista))


# def sum_minimum(lst):
#     shuma  = 0
#     for i in range(len(lst)):
#         min = lst[i][0]
#         for j in range(len(lst[i])):
#             if lst[i][j] < min:
#                 min = j
#         shuma += min
#     return shuma

# lista = [
#   [1, 2, 3, 4, 5],
#   [5, 6, 7, 8, 9],
#   [20, 21, 34, 56, 100]
# ]

# print(sum_minimum(lista))

#BINARY SEARCH
# lista = [1,2,3,4,5,6,7,8,9]

# def binary_search(n,lst):
#     first_idx = 0
#     last_idx = len(lst)
#     while first_idx < last_idx:
#         mid = (first_idx + last_idx) // 2
#         if n > lst[mid]:
#             first_idx = mid + 1
#         elif n < lst[mid]:
#             last_idx = mid
#         else:
#             return mid
        
# print(binary_search(9,lista))



# def hamming_distance(txt1, txt2):
#     count = 0
#     for i in range(len(txt1)):
#         if txt1[i] != txt2[i]:
#             count +=1
#     return count

# print(hamming_distance("abcde", "bcdef"))


def filter_list(l):
    fil= []
    for i in l:
        if not isinstance(i,str):
            fil.append(i)
    return fil

def filter_list_2(l):
    fil = filter(lambda x: type(x) != str,l)
    return list(fil)


print(filter_list([1, 2, 3, "a", "b", 4]))
print(filter_list_2([1, 2, 3, "a", "b", 4]))
















