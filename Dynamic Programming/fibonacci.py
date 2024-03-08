series = [0, 1, 1,2,3,5,8,13]
calculations = 0
def fibonacci(index):
    global calculations
    calculations += 1
    if index < 2:
        return index
    return fibonacci(index-1) + fibonacci(index-2)
    
print(fibonacci(15), calculations)

cache = {}
def dynamic_fibonacci(n):
    if n in cache:
        return cache[n]
    else:
        if n < 2:
            return n
        return dynamic_fibonacci(n-1) + dynamic_fibonacci(n-2)
        
print(dynamic_fibonacci(15))

