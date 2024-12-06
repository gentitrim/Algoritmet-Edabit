def no_duplicate_letters(phrase):
   
    for word in phrase.split():
        letters = {}
        for i in word:
            if i not in letters:
                letters[i] =  1
            else:
                letters[i] +=1
            
            for k , val in letters.items():
                if val > 1:
                    return False
    return True


print(no_duplicate_letters("Fortune favours the bold.")) # True

print(no_duplicate_letters("You can lead a horse to water, but you can't make him drink.")) # True

print(no_duplicate_letters("Look before you leap.")) # False
# Duplicate letters in "Look" and "before".

print(no_duplicate_letters("An apple a day keeps the doctor away.")) # False
# Duplicate letters in "apple", "keeps", "doctor", and "away".