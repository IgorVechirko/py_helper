def escape_symbols():
    tab_sign = "Hello \t python"
    new_line_sign = "Hello \n python"

    print("tab_sign", tab_sign)
    print("new_line_sign", new_line_sign)


def strings_init():
    str_v1 = "Hello python"
    str_v2 = 'Hello python'
    str_v3 = "Welcome \"Name\" in python"
    str_v4 = 'Welcome \'Name\' in python'
    str_v5 = "Welcome 'Name' in python"
    str_v6 = 'Welcome "Name" in python'
    """PEP 8 doesn't have recommendations for strings quotes.
       So select any"""

    str_v7 = "E:\my_projects\new_folder"
    str_v8 = r"E:\my_projects\new_folder"
    #  Error: raw string can't finish with odd escape(\)
    # str_v8 = r"E:\my_projects\new_folder\"
    # str_v8 = r'E:\my_projects\new_folder\'
    str_v9 = r"E:\my_projects\new_folder\\"

    str_v10 = """
    This is the second line of string the first one is empy.
    All previouse spaces in code will be write in console too. 
    And this is the fourth one. The last line will have some spaces.
    """
    str_v11 = """\
This is first and the only line.\
    It contain spaces from code literal. \
But it doesn't contain new line characters.\
"""

    str_v12 = ("Two string literals in role "
               'will be concatenate in one')
    str_v13 = "Two string literals in role " \
              "will be concatenate in one"
    str_v14 = str("Hello python")
    str_v15 = str(bytes(b"Hello python"), 'utf-16')
    str_v16 = str(10)
    str_v17 = str(10.654)
    str_v18 = str(6 + 4j)

    print("str_v1", str_v1)
    print("str_v2", str_v2)
    print("str_v3", str_v3)
    print("str_v4", str_v4)
    print("str_v5", str_v5)
    print("str_v6", str_v6)
    print("str_v7", str_v7)
    print("str_v8", str_v8)
    print("str_v9", str_v9)
    print("str_v10", str_v10)
    print("str_v11", str_v11)
    print("str_v12", str_v12)
    print("str_v13", str_v13)
    print("str_v14", str_v14)
    print("str_v15", str_v15)
    print("str_v16", str_v16)
    print("str_v17", str_v17)
    print("str_v18", str_v18)
    print(isinstance(str_v1, str))


def string_indexation():
    str_base = "Hello python"
    char_v1 = str_base[0]
    char_v2 = str_base[11]
    #   char_v2 = str_base[12] # Exception: out of range
    char_v3 = str_base[-1]
    #   char_v3 = str_base[-13] # Exception: out of range
    sub_str_v1 = str_base[3:7]  # slicing
    sub_str_v2 = str_base[3:]
    sub_str_v3 = str_base[:7]
    #   str_base[0] = "h" # Exception: immutable object

    print("char_v1", char_v1)
    print("char_v2", char_v2)
    print("char_v3", char_v3)
    print("sub_str_v1", sub_str_v1)
    print("sub_str_v2", sub_str_v2)
    print("sub_str_v3", sub_str_v3)


def strings_operators():
    str_v1 = "Hello " + "python"  # concatenation
    #   str_v1 = "Hello " + 5
    str_v2 = "Hello " * 5

    print("str_v1", str_v1)
    print("str_v2", str_v2)


def formatting_string():
    apple_tile = "Apple"
    apple_count = 10
    pineapple_title = "Pineapple"
    pineapple_count = 20
    melon_title = "Melon"
    melon_count = 30

    print("Fruits count:", apple_tile, "-", apple_count, ",",
          pineapple_title, "-", pineapple_count, ",",
          melon_title, "-", melon_count, ".")

    print(f"Fruits count: {apple_tile}-{apple_count}, {pineapple_title}-{pineapple_count}, {melon_title}-{melon_count}.")

    print("Fruits count: {}-{}, {}-{}, {}-{}.".format(apple_tile, apple_count,
                                                      pineapple_title, pineapple_count,
                                                      melon_title, melon_count))

    print("Fruits count: {4}-{5}, {2}-{3}, {0}-{1}.".format(apple_tile, apple_count,
                                                            pineapple_title, pineapple_count,
                                                            melon_title, melon_count))
    print("Fruits count: {2}-{3}, {2}-{3}, {0}-{1}.".format(apple_tile, apple_count,
                                                            pineapple_title, pineapple_count,
                                                            melon_title, melon_count))
    print("Fruits count: {t1}-{c1}, {t2}-{c2}, {t3}-{c3}.".format(t1=apple_tile, c1=apple_count,
                                                                  t2=pineapple_title, c2=pineapple_count,
                                                                  t3=melon_title, c3=melon_count))

    print("%d, %.1f, %s, %c, %c" % (10, 10.57654, "Hello", 65, 97))

    print("%d, %f, %.2f %s, %c, %c" % (10, 10.57654, 10.57654, "Hello", 65, 97))


def methods():
    print("Hello world".center(20))
    print("Hello world".center(10))
    print()
    print("Hello world".find("Hello"))
    print("Hello world".find("Hello", 0, 4)) # -> print("Hell", "Hello")
    print("Hello world".find("Hello", 0, 5)) # -> print("Hello", "Hello")
    print()
    print("6543".isdecimal())
    print("-6543".isdecimal())
    print("06543".isdecimal())
    print("0x6543".isdecimal())
    print("6543ab".isdecimal())
    print()
    print("Hello world".islower())
    print("hello world".islower())
    print()
    print("Hello world".isupper())
    print("HELLO WORLD".islower())
    print()
    print("Hello World".lower())
    print("Hello World".upper())
    print()
    print("Hello world and python".partition(" "))
    print("hello / world".partition("/"))
    print("hello _ world".partition("/"))
    print()
    print("Hello world".replace("world", "python"))
    print("Hello world and world".replace("world", "python"))
    print("Hello world and world".replace("world", "python", 1))



methods()