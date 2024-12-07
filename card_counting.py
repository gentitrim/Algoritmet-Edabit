'''In BlackJack, cards are counted with -1, 0, 1 values:

    2, 3, 4, 5, 6 are counted as +1
    7, 8, 9 are counted as 0
    10, J, Q, K, A are counted as -1

Create a function that counts the number and returns it from the list of cards provided.
Examples

count([5, 9, 10, 3, "J", "A", 4, 8, 5]) ➞ 1

count(["A", "A", "K", "Q", "Q", "J"]) ➞ -6'''

def count(deck):
    shuma = 0
    add_1 = [2,3,4,5,6]
    add_0 = [7,8,9]
    for i in range(len(deck)):
        if deck[i] in add_1:
            shuma +=1
        elif deck[i] in add_0:
            shuma = shuma
        else:
            shuma -= 1
    return shuma

print(count([5, 9, 10, 3, "J", "A", 4, 8, 5]))
print(count(["A", "A", "K", "Q", "Q", "J"]))