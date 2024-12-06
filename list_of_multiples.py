'''Create a function that takes two numbers as arguments (num, length) and returns a list of multiples of num until the list length reaches length.
Examples
list_of_multiples(7, 5) ➞ [7, 14, 21, 28, 35]'''

def list_of_multiples (num, length):
    return [num*i for i in range(1,length + 1)]

print(list_of_multiples(7, 5))
print(list_of_multiples(12, 10))
print(list_of_multiples(11, 21))