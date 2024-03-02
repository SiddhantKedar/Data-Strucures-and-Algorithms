def find_factorial_recursive(num):
    if num == 2:
        return 2
    if num == 1:
        return 1
    return num * find_factorial_recursive(num - 1)
    

def find_factorial_iterative(num):
    base = 1
    for i in range(num, 1, -1):
       base = base*i
    return base
       
       
iterative = find_factorial_iterative(20) 
recursive = find_factorial_recursive(20)
print(iterative)
print(recursive)
