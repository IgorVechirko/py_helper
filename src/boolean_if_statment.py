
def bool_init():
    bool_v1 = True  # Inited by boolean literal
    bool_v2 = False
    bool_v3 = bool_v1  # Inited by variable
    bool_v4 = bool(True)
    bool_v5 = bool(False)
    bool_v6 = bool(0)
    bool_v7 = bool(10)
    bool_v8 = bool(-10)
    bool_v9 = bool(0.0)
    bool_v10 = bool(0.0000000000000000000001)
    bool_v11 = bool(float("Nan"))
    bool_v12 = bool(float("inf"))
    bool_v13 = bool(float("-inf"))
    bool_v14 = bool("False")
    bool_v15 = bool("True")
    bool_v16 = bool("Not empty string")
    bool_v17 = bool("")

    print("bool_v1", bool_v1)
    print("bool_v2", bool_v2)
    print("bool_v3", bool_v3)
    print("bool_v4", bool_v4)
    print("bool_v5", bool_v5)
    print("bool_v6", bool_v6)
    print("bool_v7", bool_v7)
    print("bool_v8", bool_v8)
    print("bool_v9", bool_v9)
    print("bool_v10", bool_v10)
    print("bool_v11", bool_v11)
    print("bool_v12", bool_v12)
    print("bool_v13", bool_v13)
    print("bool_v14", bool_v14)
    print("bool_v15", bool_v15)
    print("bool_v16", bool_v16)
    print("bool_v17", bool_v17)
    print(isinstance(bool_v1, bool))


def bool_operators():#  bool/logical operators
    and_v1 = True and False
    and_v2 = False and False
    and_v3 = True and True

    print("and_v1", and_v1)
    print("and_v2", and_v2)
    print("and_v3", and_v3)

    or_v1 = True or False
    or_v2 = True or True
    or_v3 = False or False

    print("or_v1", or_v1)
    print("or_v2", or_v2)
    print("or_v3", or_v3)

    not_v1 = not True
    not_v2 = not False
    not_v3 = not not False

    print("not_v1", not_v1)
    print("not_v2", not_v2)
    print("not_v3", not_v3)

#  Boolean operators priority
#  Operator (not) has the highest priority
#  Operator (and) has lower priority
#  Operator (or) has the lowest priority
    exp_v1 = True and not False
    exp_v2 = False or not False
    exp_v3 = False or True and False

    print("exp_v1", exp_v1)
    print("exp_v2", exp_v2)
    print("exp_v3", exp_v3)


def comparison_operators():
    bool_v1 = 10 > 5
    bool_v2 = 10 >= 5
    bool_v3 = 10 < 5
    bool_v4 = 10 <= 5
    bool_v5 = 10 == 5
    bool_v5 = 10 != 5

    bool_v2 = "Hello" < "python"
    bool_v2 = "Hello" > "python"
    bool_v2 = "Python" < "python"
    bool_v2 = "Python" > "python"
    bool_v2 = "python" < "python"
    bool_v2 = "nython" > "python"
    bool_v2 = "qython" > "python"


    print("bool_v2", bool_v2)


comparison_operators()