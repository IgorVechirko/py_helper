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

vargs = ["Hello", "Python", "C++"]
default_args_func(*vargs)
kwargs = {"default_arg2": "Hello", "default_arg1": "Python", "none_default_arg": "C++"}
default_args_func(**kwargs)




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