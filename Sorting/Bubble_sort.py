numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
numbers1 = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def bubble_sort(nums):
    count = 0
    for i in range(len(nums)-1):
        print(nums)
        for j in range(len(nums)-i-1):
            count += 1
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return f"{nums}, No of comparison: {count}"


def optimized_bubble_sort(nums):
    count = 0
    for i in range(len(nums)-1):
        print(nums)
        swap = False
        for j in range(len(nums)-i-1):
            count += 1
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swap = True
        if swap == False:
            return f"{nums}, No of comparison: {count}"
    return f"{nums}, No of comparison: {count}"
    
    
print(bubble_sort(numbers))
print(optimized_bubble_sort(numbers1))
