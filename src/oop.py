def object_base_attributes():
    obj = [1, 654.3, "Python"]

    obj_type = type(obj)
    obj_id = id(obj)

    print(obj_type)
    print(obj_id)
    print(obj)


def objects_and_variables():
    variable_1 = 5  # variable referenced to object int
    print(variable_1, type(variable_1), id(variable_1))

    variable_1 = "I love Python"  # variable referenced to object str and prev object lost all referenced variables
#                                   it will be garbage collected
    print("variable_1", variable_1, type(variable_1), id(variable_1))

    variable_2 = variable_1
    variable_3 = "I love Python"
    # at this point object "I love Python" has 3 variable that referenced to him

    print("variable_2", variable_2, type(variable_2), id(variable_2))
    print("variable_3", variable_3, type(variable_3), id(variable_3))


def objects_mutability():
    pass

def attributes_and_methods():
    pass



objects_mutability()
