count = 0

def merge_sort(array):
    if len(array) == 1:
        return array
    else:
        mid = len(array)//2
        left_side = array[mid:]
        right_side = array[:mid]
        print(f'Left : {left_side}')
        print(f'Right : {right_side}')
        return merge(merge_sort(left_side), merge_sort(right_side))
        
def merge(left_side, right_side):
    l = len(left_side)
    r = len(right_side)
    left_index = 0
    right_index = 0
    sorted_array = []
    while left_index < l and right_index < r:
        global count
        count += 1
        if left_side[left_index] < right_side[right_index]:
            sorted_array.append(left_side[left_index])
            left_index += 1
        else:
            sorted_array.append(right_side[right_index])
            right_index += 1
    print(sorted_array + left_side[left_index:] + right_side[right_index:])
    return sorted_array + left_side[left_index:] + right_side[right_index:]
        
    

array = [5,9,3,10,45,2,0]
print(f"{merge_sort(array)} \nNo of comparisons {count}")

'''
Left : [10, 45, 2, 0]
Right : [5, 9, 3]
Left : [2, 0]
Right : [10, 45]
Left : [0]
Right : [2]
[0, 2]
Left : [45]
Right : [10]
[10, 45]
[0, 2, 10, 45]
Left : [9, 3]
Right : [5]
Left : [3]
Right : [9]
[3, 9]
[3, 5, 9]
[0, 2, 3, 5, 9, 10, 45]
[0, 2, 3, 5, 9, 10, 45]
'''
