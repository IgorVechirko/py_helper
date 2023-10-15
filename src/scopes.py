
sum = "global"  #shadowing builtin statement

def legb_func():
    sum = "enclosing"

    def inner_func():
        sum = "local"
        print(sum)

    return inner_func

#legb_func()()

def try_change_global_var():
    sum = "local"

def change_global_var():
    global sum
    sum = "local"

del sum


def try_modify_enclosing_var():
    enclosing_var = 20

    def inner_func():
        enclosing_var = 30

    inner_func()
    print(enclosing_var)

def modify_enclosing_var():
    enclosing_var = 20

    def inner_func():
        nonlocal enclosing_var
        enclosing_var = 30

    inner_func()
    print(enclosing_var)

#modify_enclosing_var()






"""glob = globals()
print(glob)

blob_var1 = 1
glob["glob_var2"] = 2

print(glob)
print(glob_var2)"""

def locals_sample_func():
    loc = locals()
    print(loc)

    loc_var1 = 3
    loc["loc_var2"] = 4

    print(loc)
    print(loc_var2)

#locals_sample_func()
