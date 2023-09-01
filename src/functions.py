def multiple_returns():
    val_v1 = "Python"

    if not val_v1:
        return 0

    match val_v1:
        case "Hello":
            print("Do logic v1")
            return 1
        case "world":
            return
        case _:
            print("Do uniform logic")


def default_args_func(none_default_arg, default_arg1="C++", default_arg2=2):
    print(none_default_arg, default_arg1, default_arg2)


default_args_func("Hellow")
default_args_func("Hellow", "Python")
default_args_func("Hellow", "Python", "world")
default_args_func(default_arg2="Hello", default_arg1="Python", none_default_arg="Buy buy")  # kwargs -keyworded args
default_args_func("Hello", default_arg1="Python", default_arg2="Buy buy")
default_args_func("Hello", "Python", default_arg2="Buy buy")
#default_args_func("Hello", default_arg1="Python", none_default_arg="Buy buy") danger none_default_arg specified twice

args_list = ["Hello", "Python", "C++"]
default_args_func(*args_list)
args_dict = {"default_arg2": "Hello", "default_arg1": "Python", "none_default_arg": "C++"}
default_args_func(**args_dict)

args_list = ["Hello"]
args_dict = {"default_arg1": "Python", "default_arg2": "Hello"}
default_args_func(*args_list, **args_dict)

#runtime_formed_default_val=input()
#default_dict = {"2": 2, "19": 7}
#default_val = 5
def args_func(arg_1, arg_2, arg_3=1, arg_4={}):

    if isinstance(arg_4, dict):
        arg_4.setdefault(str(len(arg_4) + 1), len(arg_4) + 1)

    print(arg_1, arg_2, arg_3, arg_4)

#args_func("Hello", "python", "C++", "Python")
#args_func("Hello", "python")

#default_val = input()
#default_dict.setdefault("654", input())


def function_as_variable(num):
    print(num, "function-variable")


value_returned_by_func = function_as_variable(1)
holded_function_var = function_as_variable
print(value_returned_by_func)
print(holded_function_var)
holded_function_var(2)

print(id(function_as_variable), id(holded_function_var))
print(type(function_as_variable), type(holded_function_var))

function_as_variable = 1  # function name is firs-class sitizen so ye we can do this
print(function_as_variable)
#function_as_variable(3)


lambda_val = lambda x, y: x + y
print(lambda_val(4, 5))


def func_with_nested_function(arg1, arg2):
    def increment(val):
        if val % 2:
            return val + 1
        else:
            return val + 2

    def decrement(val):
        if val % 2:
            return val - 1
        else:
            return val - 2

    if arg1 + arg2 > 0:
        return increment(arg1)
    elif arg1 - arg2 > 0:
        return increment(arg2)
    elif arg2 - arg1 > 0:
        return decrement(arg1)
    else:
        return decrement(arg2)


print(func_with_nested_function(5, 6))


def function_return_closures_state_inner_func(arg_var):
    func_var = 20
    def fun_with_closures_state(base):
        print(arg_var)

    return fun_with_closures_state

closures_func1 = function_return_closures_state_inner_func(10)
closures_func2 = function_return_closures_state_inner_func(50)
closures_func1(30)
closures_func2(30)


def frame_func(func):
    def exe(*vargs, **kwargs):
        print("---------->", func.__name__, "<---------", sep="")
        print()
        func(*vargs, **kwargs)
        print()
        print("<----------", func.__name__, "---------->", sep="")
        print()
    return exe

def cast_ret_to_str(func):
    def cast(*vargs, **kwargs):
        return str(func(*vargs, **kwargs)) + " str ret"
    return cast


@frame_func
def try_function(arg1):
    print("try_function", arg1)


print(try_function("python"))



def infinity_recursion(level):
    print(level)
    infinity_recursion(level + 1)


#infinity_recursion(1)


def factorial(n):

    if n < 1:
        return 0

    if n == 1:
        return n
    else:
        return n * factorial(n - 1)

print(factorial(10))




