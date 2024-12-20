from functools import cache

towels, patterns = open("data19.txt").read().split('\n\n')
towels, patterns = towels.split(', '), patterns.split('\n')

"""max_towel = -1
for towel in towels:
    if max_towel < len(towel):
        max_towel = len(towel)"""

@cache
def tracer(pattern):
    if not pattern:
        return 1
    tot=0
    for i in range(1,len(pattern)+1):
        start = pattern[:i]
        end = pattern[i:]
        if start in towels:
            tot+=tracer(end)
    return tot

part2, part1=0,0
for pattern in patterns:
    x = tracer(pattern)
    if x > 0:
        part1 +=1
    part2 += x
print(part1, part2)
