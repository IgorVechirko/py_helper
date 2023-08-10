
list_v1 = [5,3]
list_v1.append(list_v1)

print(list_v1)

list_copy = list_v1.copy()
print(list_copy)

def count_nested(list_arg):
    for elem in list_arg:
        if isinstance(elem, list):
            return 1 + count_nested(elem)

print(count_nested(list_v1))
print(count_nested(list_copy))