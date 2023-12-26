
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


def generator_from_comprehension():
    comprehension_generator = (i for i in [4, 5, 6, 3, 6])
    print(next(comprehension_generator))
    print(next(comprehension_generator))
    print(next(comprehension_generator))
    print(next(comprehension_generator))


def send_value_in_to_generator():
    def generator_func():
        val = 5
        do_work = True
        while True:
            if do_work:
                val *= val

            do_work = (yield val)

    big_num = 654320
    gen_obj = generator_func()

    gen_val = next(gen_obj)
    while gen_val < big_num:
        print(gen_val)
        gen_val = gen_obj.send(True)

    next(gen_obj)


def throw_except_in_to_generator():
    def generator_func():
        val = 5
        do_work = True
        while True:
            if do_work:
                val *= val

            do_work = (yield val)

    big_num = 654320
    gen_obj = generator_func()

    gen_val = next(gen_obj)
    while gen_val < big_num:
        print(gen_val)
        gen_val = gen_obj.send(True)

        if(len(str(gen_val)) >= 5):
            gen_obj.throw("We don't like large numbers")

    next(gen_obj)


def close_generator():
    def generator_func():
        val = 5
        do_work = True
        while True:
            if do_work:
                val *= val

            do_work = (yield val)

    big_num = 654320
    gen_obj = generator_func()

    gen_val = next(gen_obj)
    while gen_val < big_num:
        print(gen_val)
        gen_val = gen_obj.send(True)
    else:
        gen_obj.close()

    next(gen_obj)


close_generator()
