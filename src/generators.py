
def generator_function_sample():

    def generator():
        for i in (4, 2, 5, 7, 8):
            yield i

    print("New generator object returns for each generator function call")
    print(next(generator()))
    print(next(generator()))

    print("\n", "Can extrude next element from generator obj till StopIteration")
    generator_obj = generator()
    try:
        while True:
            print(next(generator_obj))
    except StopIteration:
        pass

    print("\n", "Or use in for loop")
    for i in generator():
        print(i)


generator_function_sample()