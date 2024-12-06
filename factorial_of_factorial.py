'''
Factorial of Factorials

Create a function that takes an integer n and returns the factorial of factorials. See below examples for a better understanding:
Examples

fact_of_fact(4) ➞ 288
# 4! * 3! * 2! * 1! = 288
# '''


def fact_of_fact(n):
    result = 1
    for i in range(2,n+1):
        faktori  = 1 
        for j in range(1,i+1):
            faktori *=j
        result *=faktori
    return result

print(fact_of_fact(4)) #228
print(fact_of_fact(5)) # 34560
print(fact_of_fact(6)) # 24883200