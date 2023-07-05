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


def sequences_operators():

    tuple_v1 = (544, "Hello", True)
    list_v1 = [937, "python", tuple_v1]
    range_v1 = range(0, 9)

    print("hello" in tuple_v1)
    print("python" in list_v1)
    print("sf" in range_v1)
    print()
    print("hello" not in tuple_v1)
    print("python" not in list_v1)
    print("sf" not in range_v1)
    print()
    print(tuple_v1 + tuple_v1)
    print(list_v1 + list_v1)
#   print(range_v1 + range_v1)
    print()
    print(tuple_v1 * 2)
    print(list_v1 * 2)
    print()
    print(tuple_v1[2])
    print(list_v1[2])
    print()
    print(tuple_v1[0:2])
    print(list_v1[0:2])
    print(tuple_v1[0:2:1])
    print(list_v1[0:2:2])
    print(range_v1[0:2])
    print()
    print(len(tuple_v1))
    print(min(tuple_v1))
    print(max(tuple_v1))
    print(len(list_v1))
    print(min(list_v1))
    print(max(list_v1))

sequences_operators()