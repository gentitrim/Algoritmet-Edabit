'''An isogram is a word that has no duplicate letters. Create a function that takes a string and returns either True or False depending on whether or not it's an "isogram".
Examples

is_isogram("Algorism") ➞ True

is_isogram("PasSword") ➞ False
# Not case sensitive.

is_isogram("Consecutive") ➞ False'''

def is_isogram(txt):
    letters = {}
    for i in range(len(txt)):
        if txt[i].upper() not in letters:
            letters[txt[i].upper()] = 1
        else:
            letters[txt[i].upper()] += 1

    for j in letters.values():
        if j >1:
            return False
        
    return True

print(is_isogram("Algorism"))
print(is_isogram("PasSword"))
print(is_isogram("Consecutive"))



