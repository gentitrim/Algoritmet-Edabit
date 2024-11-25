


def is_disarium(n):
    shuma = 0
    for j in range(len(str(n))):
        shuma += int(str(n)[j])**(int(j)+1)
    if shuma == n:
        return True
    return False

print(is_disarium(518))
print(is_disarium(89))
print(is_disarium(466))
    