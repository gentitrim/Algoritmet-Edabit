'''First Letter Shift
Given a sentence, create a function which shifts the first letter of each word to the next word in the sentence (shifting right).
Examples
shift_sentence("create a function") ➞ "freate c aunction"
shift_sentence("it should shift the sentence") ➞ "st ihould shift she tentence"
shift_sentence("the output is not very legible") ➞ "lhe tutput os iot nery vegible"
shift_sentence("edabit") ➞ "edabit"'''


def shift_sentence(txt):
    words = txt.split()
    first_letter = [word[0] for word in words][-1:] + [word[0] for word in words][:-1]
    for i in range(len(words)):
        words[i] = words[i][0].replace(words[i][0],first_letter[i]) + words[i][1::]
    return ' '.join(words)













print(shift_sentence("sarah the key is under the door mat"))  # "marah she tey ks inder uhe toor dat"
print(shift_sentence("the output is not very legible")) #lhe tutput os iot nery vegible