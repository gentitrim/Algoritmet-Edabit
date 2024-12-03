def truncatable(n):
    left = str(n)
    right = str(n)
    result = []
    result2  = []
    if "0" in left:
        return False
    for i in range(len(left)):
        # print(left)
        
        if int(left) >= 2 and all([(int(left))%j != 0 for j in range(2,int(int(left)**0.5) + 1)]):
            left = left[1:]
            result.append(True)
        else:
            left = left[1:]
            result.append(False)
        # print(result)
    for i in range(len(right)):
        
        if int(right) >= 2 and all([(int(right))%j != 0 for j in range(2,int(int(right)**0.5) + 1)]):
            right = right[:len(right)-1]
            result2.append(True)
        else:
            right = right[:len(right)-1]
            result2.append(False)
        print(right)
    if all(result + result2):
        return 'both'
    elif all(result):
        return "left"
    elif all(result2):
        return "right"
    else:
        return False

print(truncatable(5))
print(truncatable(317))
print(truncatable(9137))
print(truncatable(7331))

# all(map(lambda x:))