
def bool_init():
    bool_v1 = True
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
    bool_v16 = bool(str("Not empty string"))
    bool_v17 = bool(str(""))
#   tuple
    bool_v18 = bool(("", 1))
    bool_v19 = bool(())
#   list
    bool_v20 = bool([1, "", 1.1])
    bool_v21 = bool([])
#   dictionary
    bool_v22 = bool({1: "43", 2: True})
    bool_v23 = bool({})

    bool_v24 = isinstance(int(1), float)
    bool_v25 = bool(None)

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
    print("bool_v18", bool_v18)
    print("bool_v19", bool_v19)
    print("bool_v20", bool_v20)
    print("bool_v21", bool_v21)
    print("bool_v22", bool_v22)
    print("bool_v23", bool_v23)
    print("bool_v24", bool_v24)
    print("bool_v25", bool_v25)
    print(isinstance(bool_v1, bool))


def bool_operators():  # bool/logical operators
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
    bool_v6 = 10 != 5
    bool_v7 = 5 < 6 <= 10

    bool_v8 = "Hello" < "python"
    bool_v9 = "Hello" > "python"
    bool_v10 = "python" < "python"  # lexicographically comparison
    bool_v11 = "oython" > "python"  # lexicographically comparison
    bool_v12 = "qython" > "python"  # lexicographically comparison
    bool_v13 = "Python" < "python"  # lexicographically comparison
    bool_v14 = "Python" < "python" <= "oython"
    bool_v15 = "python" == "python"
    bool_v16 = "python" != "Python"

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


def if_statement():
    bool_expression = ""

    if bool_expression:
        print("bool_expression is True")
    else:
        print("bool_expression is False")

    str_v1 = "v3"
    int_v1 = 10

    if str_v1 == "v1":
        print("Do logic 1")
    elif str_v1 == "v2":
        print("Do logic 2")
    elif 0 < int_v1 < 5:
        print("Do logic 3")
    elif str_v1 == "v1" and 0 < int_v1 < 10:
        print("Do logic 4")
    else:
        print("Skip any logic")


def switch_statement():
    str_v1 = "Python"

    match str_v1:
        case "Hello":
            print("Do logi v1")
            print("continue logic v1")
        case "world":
            print("Do logic v2")
        case _:
            print("Do uniform logic")


def ternary_operator():

    val_if_true = 5
    val_if_false = "python"
    condition = val_if_false == "Python" or val_if_true == 5

    ternary_statement_ret = val_if_true if condition else val_if_false
    print(ternary_statement_ret)


switch_statement()


