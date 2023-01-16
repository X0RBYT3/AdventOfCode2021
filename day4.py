import numpy as np
from itertools import product
# I liked numpy for day 3, I will use it more often :)

with open("input.txt") as fp:
    draws = list(map(int, fp.readline().split(","))) # First drawers are seperated by commas
    # Boards are seperated by double newlines soooo
    boards = [np.mat(board.replace("\n", ";")) for board in fp.read()[1:-1].split("\n\n")]

# Using a masked Array from Numpy for this.
# Construct a masked array and then compare that against the draws
# We're using itertool's product to combine for loops
for draw, board in product(draws, [np.ma.masked_array(board) for board in boards]):
    # We're going to use a boolean operator to check against the draws
    board.mask |= board.data == draw
    # If any of these rows or columns add to 5 then we can count it as a bingo.
    # The first half of this checks against columns and the second half checks against rows.
    # Otherwise it would add up every single row and every single column
    if np.any(board.mask.sum(0) == 5) or np.any(board.mask.sum(1) == 5):
        #
        result = board.sum()*draw # Finding the answer using the board and the number just drawn
        break # product() makes this much easier

print (f"Part 1 Answer: {result}")

# For part 2 we can modify the above loop, but keep track of winning boards.

won_boards = set() # Keep track

# Reusing the same loop, but using Enumerate to find the index number as well
for draw, (idx, board) in product(draws, enumerate([np.ma.masked_array(board) for board in boards])):
    # Exact same boolean operation
    board.mask |= board.data == draw
    # Same Bingo checking
    if np.any(board.mask.sum(0) == 5) or np.any(board.mask.sum(1) == 5):
        # This is the last win.
        # Here we check for the last win, simply just by checking if it's the last board.
        if idx not in won_boards and len(won_boards) == len(boards) -1:
            result = board.sum()*draw # Find the final score of the last board.
            break
        won_boards.add(idx) # If it's not the last win, just add to the winning list.

# Spit it out.
print (f"Part 2 Answer: {result}")
