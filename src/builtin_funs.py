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




