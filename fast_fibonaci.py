'''In mathematics, the Fibonacci numbers, commonly denoted Fn, form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1:

Fibonacci Sequence

and

Fibonacci Sequence 2

for n > 1

The beginning of the sequence is thus:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

The function fib_fast(num) returns the fibonacci number Fn, of the given num as an argument.
Examples

fib_fast(5) ➞ 5
'''

def fib_fast(num):
    a , b = 0,1
    for i in range(num):
        a , b = b , a+b #(a = 1, b = 1) (a = 1 , b = 2) (a = 2, b = 3) (a = 3, b=5) (a = 5 , b = 8)
    return a



print(fib_fast(5))  #5
print(fib_fast(10))  #55
print(fib_fast(20))  #6765
