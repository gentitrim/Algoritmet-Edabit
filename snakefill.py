"""
This challenge is based on the classic videogame "Snake".
Assume the game screen is an n * n square, and the snake starts the game with length 1 (i.e. just the head) positioned on the top left corner.
For example, if n = 7 the game looks something like this:
In this version of the game, the length of the snake doubles each time it eats food (e.g. if the length is 4, after eating it becomes 8).
Create a function that takes the side n of the game screen and returns the number of times the snake can eat before it runs out of space in the game screen.
Examples
snakefill(3) ➞ 3
snakefill(6) ➞ 5
snakefill(24) ➞ 9
"""

def snakefill(n):
    area = n*n
    moves = 0
    while area>=2:
        area /= 2
        moves += 1
    return moves
    

print(snakefill(3))
print(snakefill(6))
print(snakefill(25))