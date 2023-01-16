import re
import numpy as np
# It's regex time baby


lines = open("input.txt").readlines()
# Reading these coords is a CHALLENGE.
# I could split them by "," but Regex seems more fun and challenging.
# This also has the HANDY benefit of returning them as a np array
coords = np.array([re.match('(\d+),(\d+) -> (\d+),(\d+)', line).groups() for line in lines]).astype(int) # This returns them as integer
size = np.max(coords)+1 # Find the upper bound, lower bound is 0.

# Finding Horizontal and Vertical lines
# Filter such that all coords fit (x1==x2 | y1==y2)
hv = coords[(coords[:, 0] == coords[:, 2]) | (coords[:, 1] == coords[:, 3])]

# Small range helper function
# Avoids any range(start, stop, -1) shit because it nevers works how you want it
# Basically runs range in reverse properly (hence rrange)
def rrange(start, stop):
    return range(start, stop+1) if stop >= start else range(start, stop-1, -1)

# Fill a Grid with 0s to increment
grid = np.zeros((size, size))

for x1, y1, x2, y2 in hv: # For all Horizontal and Vertical lines, increment by 1.
    grid[rrange(y1, y2), rrange(x1, x2)] += 1
result = (grid >= 2).sum() # Get all entries where value >= 2.

print (f"Part 1 Answer: {result}")

# Luckily, for part 2, We've already got the barebones code in.
# We only need to iterate through the unfiltered coords rather than the Horizonal/Vertical (hv) lines.
# Make another grid for 0s
grid = np.zeros((size, size))

for x1, y1, x2, y2 in coords: # Using unfiltered coords
    # Using the reverse range again.
    grid[rrange(y1, y2), rrange(x1, x2)] += 1

result = (grid >= 2).sum() #Exact same result finding.
print (f"Part 2 Answer: {result}")
# This Could be done neater with some more functions and shit, but I enjoy letting you guys see my working process.
