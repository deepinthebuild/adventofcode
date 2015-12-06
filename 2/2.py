def needed_paper(dim_tuple):
    side1 = dim_tuple[0] * dim_tuple[1]
    side2 = dim_tuple[1] * dim_tuple[2]
    side3 = dim_tuple[2] * dim_tuple[0]
    total = 2 * side1 + 2 * side2 + 2 * side3 + min(side1, side2, side3)
    return total

    
def needed_ribbon(dim_tuple):    
    dim_list = sorted(list(dim_tuple))
    wrap = 2 * dim_list[0] + 2 * dim_list[1]
    bow = dim_tuple[0] * dim_tuple[1] * dim_tuple[2]
    return wrap + bow
    
def parse_input(input_str):
    outstr = input_str.split('x')
    outstr = [int(x) for x in outstr]
    output = tuple(outstr)
    return output

present_list = []
    
with open("input.txt", "r") as datafile:
    for line in datafile:
        present_list.append(parse_input(line))
    
paper_list = [needed_paper(x) for x in present_list]
print("Paper Needed:", sum(paper_list))

ribbon_list = [needed_ribbon(x) for x in present_list]
print("Ribbon Needed:", sum(ribbon_list))
