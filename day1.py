# Advent of Code Day 1
def foo(l:list) -> int:
    return sum([1 if j< l[i+1] else 0 for i, j in enumerate(l[:-1])])

with open('day1input.txt') as data: sweeps = [int(x.strip()) for x in data.readlines()]

# Part 1
print(foo(sweeps))

# Part 2
print(foo([sum(sweeps[i:i+3]) for i in range(0,len(sweeps),1)]))
