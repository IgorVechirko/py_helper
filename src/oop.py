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

    variable_1 = "I love Python"  # variable referenced to object str
#                                   prev object lost all referenced variables it will be garbage collected
    print("variable_1", variable_1, type(variable_1), id(variable_1))

    variable_2 = variable_1
    variable_3 = "I love Python"
    # at this point object "I love Python" has 3 variable that referenced to him

    print("variable_2", variable_2, type(variable_2), id(variable_2))
    print("variable_3", variable_3, type(variable_3), id(variable_3))


def show_fun_affect_on_mutable_immutable_obj(mut_arg, immut_arg):
    mut_arg += ("and", "python")
    immut_arg += ("and", "python")

    print(mut_arg, type(mut_arg), id(mut_arg))
    print(immut_arg, type(immut_arg), id(immut_arg))

def objects_mutability():

    var_v1 = 5
    var_v2 = var_v1
    print(var_v1, type(var_v1), id(var_v1))
    print(var_v2, type(var_v2), id(var_v2))

    var_v1 += 1  # immutable object can't be changed. It only can be replaced
    print(var_v1, type(var_v1), id(var_v1))
    print(var_v2, type(var_v2), id(var_v2))

    print()
    print()

    var_v1 = "Hello"
    var_v2 = var_v1
    print(var_v1, type(var_v1), id(var_v1))
    print(var_v2, type(var_v2), id(var_v2))

    var_v1 += " world"  # immutable object can't be changed. It only can be replaced
    print(var_v1, type(var_v1), id(var_v1))
    print(var_v2, type(var_v2), id(var_v2))

    print()
    print()

    var_v1 = ["Hello", "world"]
    var_v2 = var_v1
    print(var_v1, type(var_v1), id(var_v1))
    print(var_v2, type(var_v2), id(var_v2))

    var_v1 += ["and", "python"]  # mutable objects can be changed
    print(var_v1, type(var_v1), id(var_v1))
    print(var_v2, type(var_v2), id(var_v2))

    print()
    print()

    mutable_obj = ["Hello", "world"]
    immutable_obj = ("Hello", "world")
    print(mutable_obj, type(mutable_obj), id(mutable_obj))
    print(immutable_obj, type(immutable_obj), id(immutable_obj))

    show_fun_affect_on_mutable_immutable_obj(mutable_obj, immutable_obj)  # in function, we can change mutable object
#                                                                           and see those changes outside the function
#                                                                           and if you try change immutable object
#                                                                           in the function the new object will be
#                                                                           created

    print(mutable_obj, type(mutable_obj), id(mutable_obj))
    print(immutable_obj, type(immutable_obj), id(immutable_obj))

objects_mutability()
