
def shuma(n):
    shuma_1 = 0
    for i in range(1,n+1):
        shuma_1 += i
    return shuma_1

print(shuma(100))

def shuma_recursion(n):
    if n <=0:
        return 0
    return n + shuma_recursion(n-1)


print(shuma_recursion(100))

