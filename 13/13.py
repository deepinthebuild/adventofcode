from collections import defaultdict
from itertools import permutations


def score_seating(input_list, scoring_dict):
    score = 0
    for index, person in enumerate(input_list):
        if index == len(input_list) - 1:
            score += scoring_dict[person][input_list[0]]
            score += scoring_dict[person][input_list[-2]]
        else:
            score += scoring_dict[person][input_list[index - 1]]
            score += scoring_dict[person][input_list[index + 1]]
    return score


pref_lookup = {"gain" : 1, "lose" : -1}
seating = defaultdict(dict)

with open("input.txt", "r") as input:
    for line in input:
        line_split = line.split()
        person = line_split[0]
        pref = line_split[2]
        amount = line_split[3]
        pairing = line_split[-1][:-1]
        
        seating[person][pairing] = pref_lookup[pref] * int(amount)


print(max(score_seating(foo, seating) for foo in permutations(list(seating.keys()))))

for key in list(seating.keys()):
    seating["Me"][key] = 0
    seating[key]["Me"] = 0
    
print(max(score_seating(foo, seating) for foo in permutations(list(seating.keys()))))
