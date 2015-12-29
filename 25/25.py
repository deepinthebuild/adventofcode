
def cantor_pair(x, y):
    x -= 1
    y -= 1
    return (((x + y) * (x + y + 1)) // 2) + y + 1
    

def nth_code(n):   
    return (20151125 * pow(252533, n-1, 33554393)) % 33554393
    

row = 2978
col = 3083

print(nth_code(cantor_pair(row, col)))

