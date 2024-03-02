# Fibonacci - the pattern of sequence is that each value is the sum of the 2 previous values, for N=5 -> 2 + 3
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

def fibonacci_iterative(n):
    array1 = [0, 1]
    for i in range(2, n+1):
        array1.append(array1[i-2] + array1[i-1])
    return array1[n]
    
def fibonacci_iterative2(n):
    first_number = 0
    second_number = 1
    if n == 0:
        return first_number
    if n == 1:
        return second_number
    for i in range(2, n+1):
        third_number = first_number + second_number
        first_number = second_number
        second_number = third_number
    return third_number
        
        
def fibonacci_recursive(n):
    if n < 2:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
        
iterative = fibonacci_iterative(7)
iterative2 = fibonacci_iterative2(7)
recursive = fibonacci_recursive(7)
print(iterative)
print(iterative2)
print(recursive)
