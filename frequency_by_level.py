def freq_count(lst,el):
    level = 0
    result = []
    for i in lst:
        if isinstance(i,list):
            level +=1 + freq_count(i,el)[0][i]
            count = i.count(el)
            result.append((level,count))
        else:
            level
            count = lst.count(el)
            result.append((level,count))
    return result

print(freq_count([1, 4, 4, [1, 1, [1, 2, [4],1, 1],4],4,4],4))

(0,4),