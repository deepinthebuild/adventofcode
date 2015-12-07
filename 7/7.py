import functools

@functools.lru_cache(maxsize=128)
def emulate(key):
    if key.isdigit():
        return int(key)
        
    elif circuit_dict[key].isdigit():
        return int(circuit_dict[key])
    
    elif 'NOT' in circuit_dict[key]:
        return ~emulate(circuit_dict[key].split()[1])
        
    elif 'AND' in circuit_dict[key]:
        return emulate(circuit_dict[key].split()[0]) & emulate(circuit_dict[key].split()[2])
    
    elif 'OR' in circuit_dict[key]:
        return emulate(circuit_dict[key].split()[0]) | emulate(circuit_dict[key].split()[2])
        
    elif 'LSHIFT' in circuit_dict[key]:
        return emulate(circuit_dict[key].split()[0]) << int(circuit_dict[key].split()[2])
        
    elif 'RSHIFT' in circuit_dict[key]:
        return emulate(circuit_dict[key].split()[0]) >> int(circuit_dict[key].split()[2])
    
    else:
        return emulate(circuit_dict[key])

circuit_dict = {}

with open("input.txt","r") as input:
    for line in input:
        circuit_dict[line.split()[-1]] = line.split('->')[0].strip()

print(emulate('a'))

circuit_dict['b'] = '3176'
emulate.cache_clear()
print(emulate('a'))