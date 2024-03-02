def reverse_string(str):
    return str[::-1]
  
def reverse_string2(str):
    final = ""
    for index in range(len(str)):
        final = final + str[len(str)-index-1]
    return final

def reverse_recursive(str):
    if len(str) == 0:
        return str
    else:
        return reverse_recursive(str[1:])+ str[0]


string = reverse_string("yoyo master")
print(string)
string2 = reverse_string2("yoyo master")
print(string2)
recursive = reverse_recursive("yoyo master")
print(recursive)


    

