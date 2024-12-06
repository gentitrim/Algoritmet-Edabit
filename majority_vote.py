'''Create a function that returns the majority vote in a list. A majority vote is an element that occurs > N/2 times in a list (where N is the length of the list).
Examples

majority_vote(["A", "A", "B"]) ➞ "A"

majority_vote(["A", "A", "A", "B", "C", "A"]) ➞ "A"

majority_vote(["A", "B", "B", "A", "C", "C"]) ➞ None'''


def majority_vote(lst):
    votes = {}
    for i in lst:
        if i not in votes:
            votes[i] = 1
        else:
            votes[i] += 1
    
    for key,val in votes.items():
        if val > len(lst)/2:
            return key
    return None


print(majority_vote(["A", "B", "B", "B", "A", "A"]))
print(majority_vote(["A", "B"]))
print(majority_vote(["A"]))