import numpy as np

data = np.loadtxt("input.txt", delimiter=",", dtype="int32") # Just load it as a list of ints
# part 1
# Fairly self explanatory little bruteforce
upper_limit = max(data) + 1

result = [np.sum(np.abs(data - i)) for i in range(upper_limit)]

print(int(np.min(result)))

# Part 2 uses Gaus' Sum, which comes from https://en.wikipedia.org/wiki/Triangular_number

gaus = lambda n: n * (n + 1) / 2
result = [np.sum(gaus(np.abs(data - i))) for i in range(upper_limit)]


print(int(np.min(result))) # part 2
