import re
import itertools as it
import collections


RUN_LENGTH = 2503
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
                    it.accumulate(it.islice(it.cycle(pattern), None))
                    for pattern in speed_generator.values()
                    )
                )
                
accum = (1 if x == max(foo) else 0 for foo in positions for x in foo)
for _ in range(18):
    print(next(accum), end = ' ')