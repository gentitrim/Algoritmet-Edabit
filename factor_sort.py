'''A numbers factor length is simply its total number of factors.

For instance:

3: 1, 3
# 3's factor length = 2

8: 1, 2, 4, 8
# 8's factor length = 4

36 : 1, 2, 3, 4, 6, 9, 12, 18, 36
# 36's factor length = 9'''


def factor_sort(nums):
    factorials = {}
    for i in nums:
        if i not in factorials:
            factorials[i]=0

        for j in range(1,i + 1):
            if i%j == 0:
                factorials[i] += 1

    # print(factorials.items())
    return list(reversed([key for key,val in sorted(factorials.items(),key=lambda item : item[1])]))

print(factor_sort([1, 2, 31, 4])) #[4, 31, 2, 1])
print(factor_sort([5, 7, 9])) #[9, 7, 5])
print(factor_sort([15, 8, 2, 3])) #[15, 8, 3, 2])
print(factor_sort([1, 2, 3, 7, 11, 13, 16])) #[16, 13, 11, 7, 3, 2, 1])
print(factor_sort([1, 5, 25, 17])) #[25, 17, 5, 1])
print(factor_sort([1, 5, 4, 17])) #[4, 17, 5, 1])