from itertools import accumulate, cycle, islice

def reindeer_race(input_list, length):
    return islice(cycle(input_list),length)


lookup = {}

with open("input.txt", "r") as input:
    for line in input:
        words = line.split()
        reindeer = words[0]
        speed = int(words[3])
        duration = int(words[6])
        rest = int(words[-2])
        lookup[reindeer] = [speed] * duration + [0] * rest


print(max(sum(reindeer_race(race, 2503)) for race in lookup.values()))

running_totals = [list(accumulate(reindeer_race(race, 2503))) for race in lookup.values()]
running_totals = list(zip(*running_totals))
points = [0] * len(list(lookup.keys()))


for position_tuple in running_totals:
    for position in range(len(points)):
        if position_tuple[position] == max(position_tuple):
            points[position] += 1

print(max(points))
