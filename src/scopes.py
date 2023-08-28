
def simple_func():
    #print(func_scope_var)

    # Function scope variables and another context
    # created for each instance of function
    func_scope_var = False
    print(func_scope_var)
    func_scope_var = True
    print(func_scope_var)


def try_use_another_func_var():
    print(func_scope_var)  # Can't access to another function scope


def blocks_as_scopes():

    condition = False

    if condition:
        true_scope_var = "Hello"
        #print(false_scope_var)
    else:
        false_scope_var = "world"
        #print(true_scope_var)

    print(false_scope_var)

    """while True:
        # for each iteration new scope created
        while_scope_var = "Python"

    print(while_scope_var)

    for i in range(0, 10):
        # for each iteration new scope created
        for_scope_var = "C++"

    print(for_scope_var)"""


blocks_as_scopes()