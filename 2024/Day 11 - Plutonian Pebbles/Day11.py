from collections import defaultdict

with open('data11.txt') as file:
    data = [int(x) for x in file.read().split()]

def stonechecker(data, times):
    stones = defaultdict(int)
    for num in data:
        stones[num] += 1
    
    for _ in range(times):
        stones_update = defaultdict(int)
        for stone, freq in stones.items():
            if stone == 0:
                stones_update[1] += freq
            elif len(str(stone)) % 2 == 0:
                L = len(str(stone))//2
                stones_update[int(str(stone)[:L])] += freq
                stones_update[int(str(stone)[L:])] += freq
            else:
                stones_update[2024*stone] += freq

        stones = stones_update
    
    return sum(freq for _, freq in stones.items())

print(stonechecker(data, 25))
print(stonechecker(data, 75))
