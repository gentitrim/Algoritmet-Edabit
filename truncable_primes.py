'''A left-truncatable prime is a prime number that contains no 0 digits and, when the first digit is successively removed, the result is always prime.

A right-truncatable prime is a prime number that contains no 0 digits and, when the last digit is successively removed, the result is always prime.

Create a function that takes an integer as an argument and:

    If the integer is only a left-truncatable prime, return "left".
    If the integer is only a right-truncatable prime, return "right".
    If the integer is both, return "both".
    Otherwise, return False.

Examples

truncatable(9137) ➞ "left"
# Because 9137, 137, 37 and 7 are all prime.

truncatable(5939) ➞ "right"
# Because 5939, 593, 59 and 5 are all prime.

truncatable(317) ➞ "both"
# Because 317, 17 and 7 are all prime and 317, 31 and 3 are all prime.'''


def truncatable(n):
    left = str(n)
    right = str(n)
    result_left = []
    result_right  = []
    if "0" in left:
        return False
    #verifikim i nese eshte left
    for i in range(len(left)):
        if int(left) >= 2 and all([(int(left))%j != 0 for j in range(2,int(int(left)**0.5) + 1)]):
            left = left[1:]
            result_left.append(True)
        else:
            left = left[1:]
            result_left.append(False)
        # print(left)

    #verifikim nese eshte right
    for i in range(len(right)):
        if int(right) >= 2 and all([(int(right))%j != 0 for j in range(2,int(int(right)**0.5) + 1)]):
            right = right[:len(right)-1]
            result_right.append(True)
        else:
            right = right[:len(right)-1]
            result_right.append(False)
        # print(right)

    #resultati final
    if all(result_left + result_right):
        return 'both'
    elif all(result_left):
        return "left"
    elif all(result_right):
        return "right"
    else:
        return False

print(truncatable(47)) #"left")
print(truncatable(347)) #"left")
print(truncatable(62383)) #"left")
print(truncatable(79)) #"right")
print(truncatable(7331)) #"right")
print(truncatable(233993)) #"right")
print(truncatable(3797)) #"both")
print(truncatable(739397)) #"both")
print(truncatable(5)) #"both", "single-digit number treated as both")
print(truncatable(349)) #False)
print(truncatable(2317))  #False, "the starting number is composite")
print(truncatable(131))   #False, "1 is not a prime")
print(truncatable(6043))  # False, "cannot contain a 0 digit")
