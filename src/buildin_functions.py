def print_func():

    print("Hello", "world", "and", "python")
    print("Hello", "world", "and", "python", sep=None)
    print("Hello", "world", "and", "python", sep=" ")
    print("Hello", "world", "and", "python", sep="")
    print("dev", "sda", "sda1", sep="/")
    print("/dev", "sda", "sda1", sep="/")
    print()

    print("Hellow world", end=None)
    print("Hellow world", end="\n")
    print("Hellow world", end="")


print_func()