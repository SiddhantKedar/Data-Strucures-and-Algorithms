
array1 = [0,3,4,31]
array2 = [4,6,30] 

def merge_sort(array1, array2):
    array_sort = array1 + array2
    array_sort.sort()
    return array_sort
   
print(merge_sort(array1, array2))  


def merge_sort2(array1, array2):
    if len(array1)==0 or len(array2)==0:
        return array1 + array2
    my_list = []
    i=0
    j=0
    
    while i<len(array1) and j<len(array2):
        if array1[i] <= array2[j]:
            my_list.append(array1[i])
            i+=1
        elif array2[j] < array1[i]:
            my_list.append(array2[j])
            j+=1
    return my_list+array1[i:]+array2[j:]
    
print(merge_sort2(array1, array2))
        
