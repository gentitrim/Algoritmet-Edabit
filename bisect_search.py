import bisect


nums = [1, 2, 2, 2, 4, 7, 9]
ind = bisect.bisect(nums, 3)

# nums.insert(ind,3) or
bisect.insort(nums,3)

print(nums)