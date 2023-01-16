import numpy as np

lines = np.loadtxt("input.txt", delimiter=",", dtype="uint32")

# This fish shit is baffling.
# I mean not really  it's basic simulation but
# You get the gist.

# We're using numpy because I happent to know part 2 is 256 iterations.
# And that's going to get RAM intensive FAST.

fish = np.zeros(9) # use Unique to return a frequency count of the fish
# This means the INDEX is the age, and the value is the count of how many fish
# The benefit of doing this like this is that when fish age, we can simply roll them along.

age, count = np.unique(lines, return_counts=True)
fish[age] = count

gen = np.copy(fish)
for _ in range(80):
    gen[7] += gen[0]
    # We can use np.roll to iterate through the fish
    gen = np.roll(gen, -1) # Move them forward one.
result = sum(gen) # Result is the sum of the fish since value is count of fish.


print (f"Part 1 Answer: {int(result)}") # Value returns a float (.0) so we int it.

# Part 2 can be approached in the EXACT same way.
# If we had done this another way, the performance would've taken a DIVE here.
#
gen = np.copy(fish)
for _ in range(256): # Obviously changing 256.
    gen[7] += gen[0]
    gen = np.roll(gen, -1)
result = sum(gen)

print (f"Part 2 Answer: {int(result)}")
