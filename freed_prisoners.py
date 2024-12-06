'''A prison can be represented as a list of cells. Each cell contains exactly one prisoner. A 1 represents an unlocked cell and a 0 represents a locked cell.

[1, 1, 0, 0, 0, 1, 0]

Starting inside the leftmost cell, you are tasked with seeing how many prisoners you can set free, with a catch. You are the prisoner in the first cell. If the first cell is locked, you cannot free anyone. Each time you free a prisoner, the locked cells become unlocked, and the unlocked cells become locked again.

So, if we use the example above:

[1, 1, 0, 0, 0, 1, 0]
# You free the prisoner in the 1st cell.

[0, 0, 1, 1, 1, 0, 1] 
# You free the prisoner in the 3rd cell (2nd one locked).

[1, 1, 0, 0, 0, 1, 0]
# You free the prisoner in the 6th cell (3rd, 4th and 5th locked).

[0, 0, 1, 1, 1, 0, 1]
# You free the prisoner in the 7th cell - and you are done!

Here, we have set free 4 prisoners in total.

Create a function that, given this unique prison arrangement, returns the number of freed prisoners.'''


def freed_prisoners(prison):
    freed = 0
    for i in range(len(prison)-1):
        if prison[i] == 1:
            freed +=1
            prison.pop(prison[i])
            if prison[i+1] == 1:
                prison[i+1] = 0
            else:
                prison[i+1] = 1
        else:
            continue
    return prison





print(freed_prisoners([1, 1, 0, 0, 0, 1, 0]))