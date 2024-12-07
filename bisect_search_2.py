import bisect

nums = [1, 2, 2, 2, 4, 7, 9]

def bin_search_bisect(lst,num):
    ind = bisect.bisect_left(lst,num)
    try:
        if lst[ind] == num:
            return ind
    except:
        return f'Elementi nuk ndodhet ne liste'
    

print(bin_search_bisect(nums,13))