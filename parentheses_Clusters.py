def split(txt):
    start = 0
    end = 1
    substring = ''
    choice = 1
    result = ""
    while end < len(txt):
        if txt[start] == "(":
            while choice >= 0:
                substring = txt[start:end]
                if substring[-1] =="(":
                    end += 1
                    choice += 1
                else:
                    end +=1
                    choice -=1
                if choice == 0:
                    result += substring
                    start = end
                    end +=1
                    break
        else:
            start+=1
            end +=1
    return result

print(split(")((()))(())()()(()(())("))