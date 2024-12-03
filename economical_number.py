def is_economical(n):
    total = 0
    for i in range(1,n):
        if n%i == 0 and is_prime(i):
            total +=len(str(i))
            # print(i)
    if len(str(n))>total:
        return "Frugal"
    elif len(str(n))==total:
        return "Equidigital"
    else:
        return "Wasteful"
    
def is_prime(m):
    if m<2 and m != 3:
        return False
    for i in range(2,int(m**0.5)+1):
        if m%i == 0:
            return False
    return True



print(is_economical(14))  # "Equidigital", "Example 
print(is_economical(125))  # "Frugal", "Example #2")
print(is_economical(30)) # "Wasteful", "Example #4")
print(is_economical(1267)) #"Equidigital"
print(is_economical(1701)) #Frugal
print(is_economical(88632)) #Wasteful
print(is_prime(9))