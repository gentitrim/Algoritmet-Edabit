'''Given a string of digits, return the longest substring with alternating odd/even or even/odd digits. If two or more substrings have the same length, return the substring that occurs first.
Examples

longest_substring("2 254 24 272163254 474 4413 38 6648 23") ➞ "272163254"
# substrings = 254,+ 272163254, 474, 41, 38, 23'''

def longest_substring(digits):
    start = 0
    result = ''
    substring = digits[0]
    # print(substring)
    for i in range(1,len(digits)):
        if (int(substring[-1])%2 == 0 and int(digits[i])%2 !=0) or (int(substring[-1])%2 != 0 and int(digits[i])%2 == 0):
            substring = digits[start:i+1]

        else:
            start = i

        if len(substring)>len(result):
            result = substring
    return result

print(longest_substring("225424272163254474441338664823")) #272163254
print(longest_substring("198644286258141856918653955964")) #2581418569
print(longest_substring("919331281193713636178478295857")) #36361
print(longest_substring("2846286484444288886666448822244466688822247"))#47