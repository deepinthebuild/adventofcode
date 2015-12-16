import re
import itertools as it
import collections
 


RUN_LENGTH = 10**6
speed_generator = collections.OrderedDict()
regex = r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.\n'


with open("input.txt", "r") as input:
    data = input.read()
    for reindeer, speed, dur, rest in re.findall(regex, data):
        speed_generator[reindeer] = it.chain(   
                                            it.repeat(int(speed), int(dur)),
                                            it.repeat(0, int(rest))
                                            )

positions = zip(   *(
                    it.accumulate(it.islice(it.cycle(pattern), RUN_LENGTH))
                    for pattern in speed_generator.values()
                    )
                )
                

points = [0] * 9
for tick in positions:
    for i, v in enumerate(tick):
        if v == max(tick):
            points[i] += 1
print(points)
print(max(points))
print([name for name in speed_generator.keys()])