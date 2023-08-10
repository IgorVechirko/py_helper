def tuple_init():
    tuple_v1 = (5, "Hello", True)
    tuple_v2 = (5, "tuple", tuple_v1)
    tuple_v3 = tuple((5, 4, 5, 6))
    tuple_v4 = tuple(tuple_v3)  # tuple
    tuple_v5 = tuple("Hello world")  # string
    tuple_v6 = tuple([783, "python", None])  # list
    tuple_v7 = tuple({783: "python", "54": None})  # dictionary
    tuple_v8 = tuple(range(0, 5))  # range

    print("tuple_v1", tuple_v1)
    print("tuple_v2", tuple_v2)
    print("tuple_v3", tuple_v3)
    print("tuple_v4", tuple_v4)
    print("tuple_v5", tuple_v5)
    print("tuple_v6", tuple_v6)
    print("tuple_v7", tuple_v7)
    print("tuple_v8", tuple_v8)
    print(isinstance(tuple_v1, tuple))


def list_init():
    list_v1 = [5, "Hello", True]
    list_v2 = [5, "tuple", list_v1]
    list_v3 = list([5, 4, 5, 6])
    list_v4 = list(list_v3)  # list
    list_v5 = list("Hello world")  # string
    list_v6 = list((783, "python", None))  # tuple
    list_v7 = list({783: "python", "54": None})  # dictionary
    list_v8 = list(range(0, 5))  # range

    print("list_v1", list_v1)
    print("list_v2", list_v2)
    print("list_v3", list_v3)
    print("list_v4", list_v4)
    print("list_v5", list_v5)
    print("list_v6", list_v6)
    print("list_v7", list_v7)
    print("list_v8", list_v8)
    print(isinstance(list_v1, list))


def range_init():
    range_v1 = range(0, 5)
    range_v2 = range(0, 5, 2)
    range_v3 = range(0, -10, -1)
#   range_v3 = range(("python", 3))
#   range_v3 = range(["python", 3])

    print("range_v1", range_v1)
    print("range_v2", range_v2)
    print("range_v3", range_v3)
    print(isinstance(range_v1, range))


def sequences_operators():

    tuple_v1 = (544, "Hello", True)
    list_v1 = [937, "python", tuple_v1]
    range_v1 = range(1, 9)
    str_v1 = "I love python"  # string implement sequences interface and can be operated with sequences operators
                              # string like a tuple it can't be modified and it can contain only symbols(characters)

    print("hello" in tuple_v1)
    print("python" in list_v1)
    print("sf" in range_v1)
    print("I lov" in str_v1)

    print()
    print("hello" not in tuple_v1)
    print("python" not in list_v1)
    print("sf" not in range_v1)
    print("I lov" not in str_v1)

    print()
    print(tuple_v1 + tuple_v1)
    print(list_v1 + list_v1)
#   print(range_v1 + range_v1)
    print(str_v1 + str_v1)

    print()
    print(tuple_v1 * 2)
    print(list_v1 * 2)
    print(str_v1 * 2)

    print()
    print(tuple_v1[2])
    print(list_v1[2])
    print(str_v1[2])
    print(range_v1[2])

    print()
    print(tuple_v1[0:2])
    print(list_v1[0:2])
    print(tuple_v1[0:2:1])
    print(list_v1[0:2:2])
    print(range_v1[0:2])

    print()
    print(len(tuple_v1))
    print(len(list_v1))
    print(len(str_v1))
    print(len(range_v1))
#   print(min(tuple_v1))  # Not comparable components. Can't compare str with int or with bool or with tuple or list
#   print(max(tuple_v1))  # Not comparable components
#   print(min(list_v1))  # Not comparable components
#   print(max(list_v1))  # Not comparable components
    print(max(range_v1))
    print(min(str_v1))
    print(max(str_v1))

    comparable_tuple = (1, 2, 3, 5, 4)
    comparable_list = ["str1", "str2", "str3"]
    print()
    print(min(comparable_tuple))
    print(max(comparable_list))

    print()
    print(tuple_v1.count(544))
    print(list_v1.count(544))
    print(range_v1.count(544))
    print(str_v1.count('o'))

    print()
    print(tuple_v1.index(544))
    #print(list_v1.index(544))
    print(range_v1.index(8))
    print(str_v1.index("p"))


def list_mutable_operators_and_methods():

    list_v1 = [5, 32, False, (5, 6), "Hello"]

    list_v1[0] = True
    print(list_v1)

    list_v1[1:3] = "string"  # right value must be iterable object with any length
    print(list_v1)
    list_v1[1:7] = (32, False)
    print(list_v1)

    list_v1.append(6.5)
    print(list_v1)

    list_v1.extend("string")  # argument must be iterable object
    # list_v1 += "string"  # the same
    print(list_v1)

    list_v1 *= 2
    print(list_v1)

    list_v1[len(list_v1)//2:] = []  # remove half of list
    print(list_v1)

    list_v1.insert(1, "Python")
    print(list_v1)
    list_v1.insert(-1, "Python")
    print(list_v1)
    list_v1.insert(100, "Python")
    print(list_v1)

    elem = list_v1.pop(2)
    print(list_v1)
    print(elem)

    # remove half of list
    new_len = len(list_v1) // 2
    while len(list_v1) > new_len:
        elem = list_v1.pop()
        print(elem)

    print(list_v1)

    list_v1.remove((5, 6))  # remove certain object
    print(list_v1)

#   if certain object doesn't exist it will throw an error
#   so to remove object safety check it existing first
    if (5, 6) in list_v1:
        list_v1.remove((5, 6))

    list_v1.reverse()
    print(list_v1)

    list_v1.clear()
    print(list_v1)


def tips():
    col = (5, 6, 7)
    var_v1, var_v2, var_v3 = col

    print(var_v1)
    print(var_v2)
    print(var_v3)


tips()