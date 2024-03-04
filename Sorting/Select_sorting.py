numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def selection_sort(nums):
    count = 0
    for i in range(len(nums)-1):
        print(nums)
        minimum_num = nums[i]
        minimum_index = i
        for j in range(i+1, len(nums)):
            count += 1
            if nums[j] < minimum_num:
                minimum_num = nums[j]
                minimum_index = j
        if minimum_index != i:
            nums[minimum_index], nums[i] = nums[i], nums[minimum_index]
            
    return f"{nums}, No of comparisons: {count}"
        
        
print(selection_sort(numbers))
