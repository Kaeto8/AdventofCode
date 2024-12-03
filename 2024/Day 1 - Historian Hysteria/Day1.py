with open('data1.txt') as file:
    data = file.readlines()

total = 0
left, right = [], []

for line in data:
    line = line.strip().split()
    left.append(int(line[0]))
    right.append(int(line[1]))

left = sorted(left)
right = sorted(right)

for i in range(len(left)):
    total += abs(left[i]-right[i])

print("Part 1: " +str(total))

#....................Part 2............................

total2 = 0

for i in range(len(left)):
    total2 += left[i] * right.count(left[i])

print("Part 2: " +str(total2))
