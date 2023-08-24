import copy


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
    # print(list_v1.index(544))
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

    list_v1 += (5, 32)
    list_v1[-3:-1:1] = (0, 0)
    print(list_v1)

    list_v1[-3:-1] = []
    print(list_v1)

    list_v1.append(6.5)
    print(list_v1)

    list_v1.extend("string")  # argument must be iterable object
    # list_v1 += "string"  # the same
    print(list_v1)

    list_v1 *= 2
    print(list_v1)

    list_v1[len(list_v1) // 2:] = []  # remove half of list
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


def collections_copy():
    nested_list = ["Hellow", "world", ["By", "by"]]
    list_v1 = [5, 6, 7, 6, (True, False), nested_list]
    list_v2 = list_v1

    print(id(list_v1))
    print(id(list_v2))

    list_copy_v1 = []
    for elem in list_v1:
        list_copy_v1.append(elem)

    list_copy_v1.remove(6)
    nested_list[1] = "python"

    print(id(list_v1), list_v1)
    print(id(list_copy_v1), list_copy_v1)

    list_copy_v2 = list_v1.copy()  # perform shallow(not deep) copy

    nested_list[1] = "C++"

    print(id(list_v1), list_v1)
    print(id(list_copy_v2), list_copy_v2)

    list_copy_v3 = copy.copy(list_v1)  # shallow
    list_copy_v4 = list_v1[:]  # shallow

    nested_list[1] = "Java"

    print(id(list_copy_v3), list_copy_v3)
    print(id(list_copy_v4), list_copy_v4)

    list_copy_v5 = copy.deepcopy(list_v1)

    nested_list[2][1] = "beautiful"

    print(id(list_copy_v3), list_copy_v3)
    print(id(list_copy_v5), list_copy_v5)

    tuple_v1 = (5, False, nested_list)
    tuple_v2 = tuple_v1
    tuple_v3 = copy.copy(tuple_v2)
    tuple_v4 = copy.deepcopy(tuple_v3)

    nested_list[2][1] = "ugly"

    print(id(tuple_v1), tuple_v1)
    print(id(tuple_v2), tuple_v2)
    print(id(tuple_v3), tuple_v3)
    print(id(tuple_v4), tuple_v4)


def dictionary_collection():
    # Dictionary is a key-value type or mapping type
    # 'key' must be a hashable type and 'value' can be any type
    # Only immutable objects can be hashable
    dict_v1 = {56: "Hello world",  # 'key' is int
               1.56: [3, 2, 1],  # 'key' is float
               "Hello": 6.6,  # 'key' is str
               True: (5, 4, 0),  # 'key' is bool
               None: False,  # 'key' is NoneType
               (4, 6, 7): None}  # 'key' is tuple. Tuple hashable only if neaster object are hashable too

    dict_v2 = dict({56: "Hello",
                    2.65: "world"})
    dict_v3 = dict([(56, "Hello"), (2.65, "world"), (None, False)])
    dict_v4 = dict(foo=100, bar=200)

    dict_v5 = {x: x ** 2 for x in range(10)}

    print(dict_v1)
    print(dict_v2)
    print(dict_v3)
    print(dict_v4)
    print(dict_v5)
    print(isinstance(dict_v1, dict))


def dict_operators():
    dict_v1 = {5: "Hello world",
               1.56: [3, 2, 1],
               "Hello": 6.6,
               True: (5, 4, 0),
               None: False,
               (4, 6, 7): None}

    print(dict_v1[5])

    dict_v1[5] = "Python"
    print(dict_v1[(4, 6, 7)])

#    print(dict_v1[83653]) danger

    if 83653 in dict_v1:
        print(dict_v1[83653])

    if 83653 not in dict_v1:
        dict_v1[83653] = None  # insertion
        print(dict_v1[83653])

    dict_v2 = {x: x**2 for x in range(0, 10)}

    dict_v3 = dict_v1 | dict_v2  # keys from dict_v2 has higher priority
    print(dict_v3)

    dict_v1 |= dict_v2

    print(dict_v1)


def dict_methods():

    dict_v1 = {5: "Hello world",
               1.56: [3, 2, 1],
               "Hello": 6.6,
               True: (5, 4, 0),
               None: False,
               (4, 6, 7): None}

    print(list(dict_v1))
    print(len(dict_v1))

    dict_v2 = dict_v1.copy()
    print(id(dict_v1), id(dict_v2))

    print(dict_v1.get(5))
    print(dict_v1.get(6, "Default value"))
    print(dict_v1.get(6))
    print()

    items_view = dict_v1.items()
    keys_view = dict_v1.keys()  # != list(dict_v1)
    values_view = dict_v1.values()
    print(items_view)
    print(keys_view)
    print(values_view)
    dict_v1[90] = "100500"
    print(items_view)
    print(keys_view)
    print(values_view)
    print()


    print(dict_v1.pop(5), dict_v1)
    print(dict_v1.pop(6, "Default value"))
#    print(dict_v1.pop(6)) danger

    dict_v2[6] = 67890
    while len(dict_v2):
        print(dict_v2.popitem())
    print()

    return_def_val = dict_v1.setdefault(876543, "Value")
    print(return_def_val, dict_v1)

    dict_v1.update(dict_v2)  # dict_v1 |= dict_v2
    print(dict_v1)

    dict_v1.clear()
    print(dict_v1)
    print()

    print(dict(zip((1, 2, 3, 4, 5), ("Hellow", "world", "python"))))
    print(dict(zip(range(0, 100), ("Hellow", "world", "python"))))


def set_collection():

    set_v1 = {1, 5.6, False, None, (543, 93)}  # can contain hashable objects
    set_v2 = {(6, "Hello", None)}
    set_v3 = set([6, "hello", None])
    set_v4 = set({65: "hello", "world": 5.45})
    set_v5 = {c for c in 'abracadabra' if c not in 'abc'}

    print(set_v1)
    print(set_v2)
    print(set_v3)
    print(set_v4)
    print(set_v5)

    print(isinstance(set_v1, set))


def set_operators():
    set_v1 = {1, 2, 3, 4}
    set_v2 = {1, 2, 3, 4, 5, 6, 7, 8}
    set_v3 = {4, 8, 9, 10, 11, 12}

    print(5 in set_v1)
    print(5 not in set_v1)
    print()

    print(set_v1 <= set_v2)
    print(set_v1 <= set_v1)
    print(set_v2 <= set_v1)
    print(set_v1 < set_v1)
    print()

    print(set_v1 >= set_v2)
    print(set_v1 >= set_v1)
    print(set_v2 >= set_v1)
    print(set_v1 > set_v1)
    print()

    union = set_v1 | set_v2 | set_v3
    print(union)
    union |= union
    print()

    intersection = set_v1 & set_v2 & set_v3
    print(intersection)
    intersection &= intersection
    print()

    diff = set_v3 - set_v2 - set_v1
    print(diff)
    diff -= diff
    print()

    symmetric_diff = set_v1 ^ set_v2 ^ set_v3
    print(symmetric_diff)
    symmetric_diff ^= symmetric_diff
    print()


def set_methods():
    set_v1 = {1, 2, 3, 4}
    set_v2 = {1, 2, 3, 4, 5, 6, 7, 8}
    set_v3 = {4, 8, 9, 10, 11, 12}

    print(len(set_v1))
    print()

    print(set_v1.isdisjoint(set_v2))
    # the same
    print(False if len(set_v1 & set_v2) else True)
    print()

    print(set_v1.issubset(set_v2))
    # the same
    print(set_v1 <= set_v2)
    print()

    print(set_v1.issuperset(set_v2))
    # the same
    print(set_v1 >= set_v2)
    print()

    union = set_v1.union(set_v2, set_v3)
    # the same
    #union = set_v1 | set_v2 | set_v3
    print(union)
    print()

    intersection = set_v1.intersection(set_v2, set_v3)
    # the same
    # intersection = set_v1 & set_v2 & set_v3
    print(union)
    print()

    diff = set_v1.difference(set_v2, set_v3)
    # the same
    # diff = set_v1 - set_v2 - set_v3
    print(diff)
    print()

    diff = set_v1.symmetric_difference(set_v2)
    # the same
    # diff = set_v1 ^ set_v2
    print(diff)
    print()

    set_v1.update({21, 22, 23}, {24, 25, 26})
    #the same
    #set_v1 |= {21, 22, 23} | {24, 25, 26}
    print(set_v1)
    print()

    set_v1.intersection_update({21, 22, 23}, {24, 25, 26})
    # the same
    # set_v1 &= {21, 22, 23} & {24, 25, 26}
    print(set_v1)
    print()

    set_v1.difference_update({21, 22, 23}, {24, 25, 26})
    # the same
    # set_v1 -= {21, 22, 23} | {24, 25, 26}
    print(set_v1)
    print()

    set_v1.symmetric_difference_update({21, 22, 23})
    # the same
    # set_v1 ^= {21, 22, 23}
    print(set_v1)
    print()

    set_v1.add(0)
    print(set_v1)
    set_v1.remove(0)
    print(set_v1)

    #set_v1.remove(1) danger
    if 1 in set_v1:
        set_v1.remove(1)
    set_v1.discard(1)
    print(set_v1)
    print()

    print(set_v1.pop())  # if pop empy set error occur
    if len(set_v1):
        set_v1.pop()
    print(set_v1)
    print()

    set_v1.clear()
    print(set_v1)


def tips():
    col = (5, 6, 7)
    var_v1, var_v2, var_v3 = col

    print(var_v1)
    print(var_v2)
    print(var_v3)


set_methods()
