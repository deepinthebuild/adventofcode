from itertools import permutations


def node_distance(node1, node2):
    for edge in edges:
        if node1 in edge and node2 in edge:
            return edge[2]

def path_distance(nodes):
    return sum(node_distance(nodes[k], nodes[k+1]) for k in range(len(nodes) - 1))

    
    
    
    


edges = []
nodes = set()

with open("input.txt", "rt") as input:
    for line in input:
        source, dest, weight = line.split()[::2]
        edges.append((source, dest, int(weight)))
        nodes.add(source)
        nodes.add(dest)

nodes = list(nodes)



print(min(path_distance(node_list) for node_list in permutations(nodes)))
print(max(path_distance(node_list) for node_list in permutations(nodes)))
