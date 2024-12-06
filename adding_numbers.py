"""
Create a function that takes two number strings and returns their sum as a string.
Examples
add("111", "111") ➞ "222"
add("10", "80") ➞ "90"
add("", "20") ➞ "Invalid Operation"
Notes
If any input is "" or None, return "Invalid Operation".
"""

def add(n1, n2):
    if all([n1!="",n2!="",n1 !=None,n2 != None]):
        return str(int(n1) + int(n2))
    return "Invalid operation"

print(add("","20"))
print(add("10","80"))
print(add("111","111"))
print(add(None,"111"))