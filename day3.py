# Going to use Numpy to flex
import numpy as np

lines = np.loadtxt("input.txt", "U")
bits = int(len(lines[0])) #array(['011010010110', '1011101001s10',...])
# Reshape the data.
data = lines.view('U1').astype(int).reshape(lines.shape[0], bits)

pow2 = 1<<np.arange(bits)[::-1] # Fast Binary Converter.


ones = (data == 1).sum(axis=0)
zeros = (data == 0).sum(axis=0)
# Convert to int and multiply for result
result = pow2.dot(ones > zeros) * pow2.dot(ones < zeros)

print (f"Part 1 Answer: {result}")

# Part 2 is bs
# Sorry.

majo = mino = data # Divide columns into majo and mino
# I would use min but that's a builtin
for idx in range(bits):
    majcol = majo[:, idx] # majo for Majority
    mincol = mino[:, idx] # mino for Minority
    # We compare the sum of the column with half the length of the column to see if the number is majo majority
    # We do this until majo is only 1 entry.
    majo = majo[majcol == (majcol.sum()*2 >= majcol.size)] if len(majo) > 1 else majo # Find Majority

    # Now we do the same, but in reverse for finding the minority of majo column.
    # Again, until mino is only 1 column.
    mino = mino[mincol == (mincol.sum()*2 < mincol.size)] if len(mino) > 1 else mino # Find Minority.

# We convert this to int and multiply them.
result = pow2.dot(majo[0] == 1) * pow2.dot(mino[0] == 1)
print (f"Part 2 Answer: {result}")
