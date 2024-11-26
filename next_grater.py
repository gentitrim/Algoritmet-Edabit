"""You are given two numbers a and b. Create a function that returns the next number greater than a and b and divisible by b.
Examples
divisible_by_b(17, 8) ➞ 24
divisible_by_b(98, 3) ➞ 99
divisible_by_b(14, 11) ➞ 22"""


def divisible_by_b(a, b):
	return (int(a/b) + 1)*b

print(divisible_by_b(17, 8))
print(divisible_by_b(98, 3))
print(divisible_by_b(14, 11))
print(divisible_by_b(8, 8))