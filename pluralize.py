'''Given a list of words in the singular form, return a set of those words in the plural form if they appear more than once in the list.
Examples

pluralize(["cow", "pig", "cow", "cow"]) ➞ { "cows", "pig" }'''

def pluralize(lst):
    result = set()
    for i in set(lst):
        if lst.count(i) > 1:
            result.add(i + "s") 
        else:
            result.add(i)  
    return result

print(pluralize(["cow", "pig", "cow", "cow"]))