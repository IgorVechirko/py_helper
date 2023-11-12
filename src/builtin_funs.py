import copy
import sys

def abs_builtin():
    print(abs(-3))
    print(abs(-3.6))
    print(abs(-3.6+6j))


def all_builtin():
    print(all([1, 7, 8, 4]))
    print(all((1, 7, 8, 0)))
    print(all([]))
    print(all({5, 7, 4, None, 0}))
    print(all({"1": "out", "2": "in"}))


def any_builtin():
    print(any([1, 7, 8, 4]))
    print(any((0, 0, 8, 0)))
    print(any([]))
    print(any({0, 0, 0, 0, 0}))
    print(any({"1": "out", "2": "in"}))


def ascii_builtin():
    print(ascii("chars: \n \t \b"))


def bin_builtin():
    bin_str = bin(3)
    print(bin_str)
    print(int(bin_str, 2))


def enumerate_builtin():
    list_var = ["Spring", "Summer", "Fall", "Winter"]
    enumeration = enumerate(list_var, 6)
    enumerated_list = list(enumeration)
    print(enumerated_list)
    print(dict(enumerated_list))


def filter_builtin():
    filtering_coll = {5, 3, 6, 2, 7, 34, 65, 65, 1, 2}
    filtered_coll = list(filter(lambda x: not x % 2, filtering_coll))
    print(filtered_coll)


def hash_and_hex_builtins():
    obj = (1, "one", 2, "tow", 3, "three")
    object_hash = hash(obj)
    print(hex(object_hash))


def map_and_next_builtin():
    numbers1 = [1, 2, 3, 4, 5]
    numbers2 = [10, 20, 30, 40, 50]
    numbers3 = [100, 200, 300, 400, 500]

    iterator = map(lambda x, y, z: x + y + z, numbers1, numbers2, numbers3)

    list_1 = list(iterator)
    print(list_1)

    iterator = map(lambda x, y, z: x + y + z, numbers1, numbers2, numbers3)

    list_2 = []
    try:
        while(True):
            list_2.append(next(iterator))
    except StopIteration:
        print(list_2)

    iterator = map(lambda x, y, z: x + y + z, numbers1, numbers2, numbers3)
    list_3 = []

    value = next(iterator, StopIteration())
    while not isinstance(value, StopIteration):
        list_3.append(value)
        value = next(iterator, StopIteration())

    print(list_3)


def max_min_builtin():
    list_var = [4, 5, 3, 2, 54, 43, 5]

    print(max(list_var))
    print(min(4, 3, 5, 2, 0, 2, 5, 2))

    try:
        print(max([]))
    except ValueError:
        print("Empty iterable")

    print(min([], default=None))

    print(max((5, 3), (8, 3), (9, 1), (8, 4), (8, 3), key=lambda x: x[0]))


def oct_builtin():
    print(oct(378909))


def repr_builtin():
    print(list(repr("Hello python")))


def reversed_builtin():
    print("".join(reversed("Hello python")))


def round_builtin():
    print(round(7.837483654, 5))
    print(round(7.837483654))


def sorted_builtin():
    raw_list = [54, 3, 6543, 3, 6, 2, 6, 343434, 63]

    sorted_1 = sorted(raw_list)
    sorted_2 = sorted(raw_list, reverse=True)
    sorted_3 = sorted(raw_list, key=lambda x: -x)

    print(sorted_1)
    print(sorted_2)
    print(sorted_3)


def sum_builtin():
    print(sum([54, 3, 6543, 3, 6, 2, 6, 343434, 63]))


