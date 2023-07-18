
tuple_v1 = (547, "Python", True)
list_v1 = [546, "I love python", tuple_v1]
str_v1 = "Python is BS"
range_v1 = range(39, -57, -6)

#for tuple_elem in tuple_v1:
#    print(tuple_elem)

#for tuple_elem in range_v1:  # key word 'in' has not the same effect as word 'in' in this case '547 in tuple_v1'
#    print(tuple_elem)

concat_collection = list_v1 + list(tuple_v1)
concat_collection_len = len(list_v1) + len(tuple_v1)

for list_indx in range(0, concat_collection_len):
    if list_indx % 2:
        print(concat_collection[list_indx])

