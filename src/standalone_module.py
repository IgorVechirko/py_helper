
exported_var = "Hello module"
_not_exported_var = "Not exported"  # Because underscore in front

def exported_func(arg1, arg2):
    if arg1:
        print(arg2 * 2)


class ExportedClass:
    def __init__(self):
        print("Construct exported class")


    def exe(self):
        print(exported_var)


print("Module has been run somehow")

if(__name__ == "__main__"):
    print("Module has been run like a script")
else:
    print("Module has been import")
