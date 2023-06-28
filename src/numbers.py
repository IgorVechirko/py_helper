
def int_init():

    int_v1 = 10  # Inited by numeric literal
    int_v2 = int_v1  # Inited by another variable
    int_v3 = int(10)
    int_v4 = int(int_v1)
    int_v5 = int("11")  # Inited by string literal
    int_v6 = int("-11", 10)
    int_str = "-11"
    int_v7 = int(int_str)  # Inited by string

    int_64_bit = 2 ** 64
    int_big = 2 ** 100
    int_small = -(2 ** 100)

    print("int_v1", int_v1)
    print("int_v2", int_v2)
    print("int_v3", int_v3)
    print("int_v4", int_v4)
    print("int_v5", int_v5)
    print("int_v6", int_v6)
    print("int_v7", int_v7)
    print("int_v7", int_v7)
    print("int_v7", int_v7)
    print("int_64_bit", int_64_bit)
    print("int_big", int_big)
    print("int_small", int_small)
    print(isinstance(int_v1, int))
    print()


# 8base
    int_8base_v1 = 0o346
    int_8base_v2 = 0O346
    int_8base_v3 = int("346", 8)
    int_8base_v4 = int("0o346", 8)
    int_8base_v5 = int("-0O346", 8)
    # int_8base_v5 = int("0o346") #Error: Default base is 10.
    #                                  Invalid string for 10 base.
    # int_8base_v5 = int("0o348", 8) #Error: Unsuitable character
    #                                    "8" in string.

    print("int_8base_v1", int_8base_v1)
    print("int_8base_v2", int_8base_v2)
    print("int_8base_v3", int_8base_v3)
    print("int_8base_v4", int_8base_v4)
    print("int_8base_v5", int_8base_v5)
    print()

# 16 base
    int_16base_v1 = 0xAF47
    int_16base_v2 = 0XAF47
    int_16base_v3 = int("346", 16)
    int_16base_v4 = int("0xAF47", 16)
    int_16base_v5 = int("-0XAF47", 16)
    # int_16base_v3 = int("0xAF47") #Error: Default base is 10. Invalid string for 10 base.
    # int_16base_v3 = int("0xAF4G", 16) #Error: Unsuitable character
    #                                       "G" in string.

    print("int_16base_v1", int_16base_v1)
    print("int_16base_v2", int_16base_v2)
    print("int_16base_v3", int_16base_v3)
    print("int_16base_v4", int_16base_v4)
    print("int_16base_v5", int_16base_v5)
    print()

# 2 base
    int_bin_base_v1 = 0b10101
    int_bin_base_v2 = 0B10101
    int_bin_base_v3 = int("10101", 2)
    int_bin_base_v4 = int("0b10101", 2)
    int_bin_base_v5 = int("-0B10101", 2)
    # int_bin_base_v3 = int("0b10101") #Error: Default base is 10. Invalid string for 10 base.
    # int_bin_base_v3 = int("0b10102", 2) #Error: Unsuitable character
    #                                         "2" in string.

    print("int_bin_base_v2", int_bin_base_v2)
    print("int_bin_base_v3", int_bin_base_v3)
    print("int_bin_base_v4", int_bin_base_v4)
    print("int_bin_base_v1", int_bin_base_v1)
    print("int_bin_base_v5", int_bin_base_v5)
    print()


def flt_init():

    flt_v1 = 45.36  # Inited by numeric literal
    flt_v2 = 45.
    flt_v3 = 1e-003
    flt_v4 = 17653E-2
    flt_v5 = 17653E2
    flt_v6 = flt_v1  # Inited by another variable
    flt_v7 = float(863e-1)
    flt_v8 = float(flt_v7)
    flt_v9 = float("1")
    flt_v10 = float("+1.")
    flt_v11 = float("-54.2")
    flt_v12 = float("-134e-2")
    flt_v13 = float("nan")
    flt_v14 = float("-Nan")
    flt_v15 = float("+NaN")
    # flt_v13 = float("")
    # flt_v13 = float("ny5") # Error: Unsuitable literal for float
    flt_v16 = float("inf")
    flt_v17 = float("-inf")
    flt_v18 = float("+inf")
    flt_v19 = float("InFiNiTy")
    flt_v20 = 0.0

    print("flt_v1", flt_v1)
    print("flt_v2", flt_v2)
    print("flt_v3", flt_v3)
    print("flt_v4", flt_v4)
    print("flt_v5", flt_v5)
    print("flt_v6", flt_v6)
    print("flt_v7", flt_v7)
    print("flt_v8", flt_v8)
    print("flt_v9", flt_v9)
    print("flt_v10", flt_v10)
    print("flt_v11", flt_v11)
    print("flt_v12", flt_v12)
    print("flt_v13", flt_v13)
    print("flt_v14", flt_v14)
    print("flt_v15", flt_v15)
    print("flt_v16", flt_v16)
    print("flt_v17", flt_v17)
    print("flt_v18", flt_v18)
    print("flt_v19", flt_v19)
    print("flt_v20", flt_v20)
    print(isinstance(flt_v1, float))


def complex_init():

    complex_v1 = 3 + 4j
    complex_v2 = 4j
    complex_v3 = complex(2, 4)
    complex_v4 = complex("3+4j")
    complex_v5 = complex("-3-4j")

    print("complex_v1", complex_v1)
    print("complex_v2", complex_v2)
    print("complex_v3", complex_v3)
    print("complex_v4", complex_v4)
    print("complex_v5", complex_v5)


def arithmetic_operators():

    var_v1 = 6
    var_v2 = 2
    var_v3 = 5

    """
    var_v1 = 6
    var_v2 = 2
    var_v3 = 5.0
    """

    """
    var_v1 = 6.0
    var_v2 = 2.0
    var_v3 = 5.0
    """

    ret_v1 = var_v1 + var_v2
    ret_v2 = var_v1 - var_v2
    ret_v3 = var_v1 * var_v2
    ret_v4 = var_v3 / var_v2
    ret_v5 = var_v3 // var_v2  # floored quotient
    ret_v6 = var_v3 % var_v2  # remainder
    ret_v7 = divmod(var_v3, var_v2)
    ret_v8 = -var_v1
    ret_v9 = +var_v1
    ret_v10 = abs(-var_v1)
    ret_v11 = pow(var_v3, var_v2)
    ret_v12 = var_v3 ** var_v2

    print("ret_v1", ret_v1)
    print("ret_v2", ret_v2)
    print("ret_v3", ret_v3)
    print("ret_v4", ret_v4)
    print("ret_v5", ret_v5)
    print("ret_v6", ret_v6)
    print("ret_v7", ret_v7)
    print("ret_v8", ret_v8)
    print("ret_v9", ret_v9)
    print("ret_v10", ret_v10)
    print("ret_v11", ret_v11)
    print("ret_v12", ret_v12)


def operators_precedence():

    ret_v1 = 2 + 5
    ret_v2 = 2 + 5 - 7
    ret_v3 = 2 + 5 - 7 * 2
    ret_v4 = 2 + 5 - 7 * 2 / 4
    #  For all operators precedence look for doc

    ret_v5 = ((2 + 5) - (7 * 2)) / 4

    prt_v1 = 2 + 5
    prt_v2 = 7 * 2
    prt_v3 = prt_v1 - prt_v2
    ret_v6 = prt_v3 / 4

    print("ret_v1", ret_v1)
    print("ret_v2", ret_v2)
    print("ret_v3", ret_v3)
    print("ret_v4", ret_v4)
    print("ret_v5", ret_v5)
    print("ret_v6", ret_v6)


operators_precedence()
