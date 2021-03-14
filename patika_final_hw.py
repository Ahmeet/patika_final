l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flat_list = []

def flatten_list(data):
    for element in data:
        if type(element) == list:
            flatten_list(element)
        else:
            flat_list.append(element)
            
            
flatten_list(l)
print(flat_list)


l = [[1, 2], [3, 4], [5, 6, 7]]


def reverse_list(data):
    reversed_list = []
    for element in data:
        if isinstance(element, list):
            reversed_list.append(reverse_list(element))
        else:
            reversed_list.append(element)
    reversed_list.reverse()
    return reversed_list
    

print(reverse_list(l))
