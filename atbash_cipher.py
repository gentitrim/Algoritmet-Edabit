""" The Atbash cipher is an encryption method in which each letter of a word is replaced with its "mirror" letter in the alphabet: A <=> Z; B <=> Y; C <=> X; etc.
Create a function that takes a string and applies the Atbash cipher to it.
Examples
atbash("apple") ➞ "zkkov"
atbash("Hello world!") ➞ "Svool dliow!"
atbash("Christmas is the 25th of December") ➞ "Xsirhgnzh rh gsv 25gs lu Wvxvnyvi """


def atbash(txt):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    cipher = []
    for i in txt:
        if i not in alpha and i not in [j.upper() for j in alpha]:
            cipher.append(i)
        elif i.islower() :
            cipher.append(alpha[-(alpha.index(i)) - 1])
        else:
            cipher.append(alpha[-(alpha.index(i.lower())) - 1].upper())
    return "".join(cipher)

print(atbash("Hello world!"))
print(atbash("Christmas is the 25th of December"))

