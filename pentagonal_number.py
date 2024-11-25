def pentagonal(num):
    pikat = 1
    for i in range(num):
        pikat += 5*i
    return pikat


print(pentagonal(21))