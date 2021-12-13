#Advent of Code Day 2
with open('day2input.txt') as data: di = [i.strip() for i in data.readlines()]
# Part 1

d=[int(l.split()[1]) if 'fo' in l else (int(l.split()[1]) * 1j if 'do' in l else ( -int(l.split()[1]) * 1j if 'up' in l else l)) for l in di]
print((lambda j: j.imag * j.real)(sum(d)))

# Part 2
p= sum(z.real * (1 + 1j * a) for z, a in zip(d, [sum(d[: i + 1]).imag for i in range(len(d))]))
print(p.real * p.imag)

