numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def insertion_sort(numbers):
    count = 0
    for i in range(1, len(numbers)):
        print(numbers) 
        last_sorted = numbers[i-1]
        count += 1
        if numbers[i] < last_sorted:
            temp = numbers[i]
            for j in range(i-1,-1,-1):
                count += 1
                if temp < numbers[j]:
                    if j == 0:
                        numbers[j+1] = numbers[j]
                        numbers[j] = temp
                    else:
                        numbers[j+1] = numbers[j]
                        
                else:
                    numbers[j+1] = temp
                    break
    return f"{numbers} \nNo of comparisons {count}"
    
    
print(insertion_sort(numbers))
