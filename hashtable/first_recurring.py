array1 = [2,5,1,2,3,5,1,2,4]
array2 = [2,1,1,2,3,5,1,2,4]

# brute force
def first_recurring(array):
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            if array[i] == array[j]:
                return array[i]
    return None

# with hashtable
def first_recurring2(array):
    dict = {}
    for i in range(len(array)):
        print(dict)
        if array[i] in dict:
            return array[i]
        else:
            dict[array[i]] = i
    
    return -1
    
print(first_recurring2(array1))
