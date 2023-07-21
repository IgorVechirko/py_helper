
def for_statement():

    tuple_v1 = (547, "Python", True)
    list_v1 = [546, "I love python", tuple_v1]
    str_v1 = "Python is BS"
    range_v1 = range(19, -19, -6)

    for elem in tuple_v1:  # key word 'in' has not the same effect as word 'in' in this case '547 in tuple_v1'
        print(elem)
    else:
        print()

    for elem in list_v1:
        print(elem)
    else:
        print()

    for elem in str_v1:
        print(elem)
    else:
        print()

    for elem in range_v1:
        print(elem)
    else:
        print()


def while_statement():
    list_v1 = [684, "C++", False]
    tuple_v1 = (547, "Python", list_v1, True)

    #  while loop commonly used in case when you don't know amount of loop iteration needed to complete the work
    tuple_idx = 0
    while tuple_idx < len(tuple_v1) and not isinstance(tuple_v1[tuple_idx], list):

        print(tuple_v1[tuple_idx])
        tuple_idx += 1
    else:
        print("'while' execution finish")

    print()

    #  while loop behavior can be emulated with for loop and break statement
    for elem in tuple_v1:

        if isinstance(elem, list):
            break

        print(elem)
    else:
        print("for execution finish")



def continue_statement():
    tuple_v1 = (547, "Python", True)
    list_v1 = [546, "I love python", tuple_v1]

    for elem in tuple_v1:
        if not isinstance(elem, str):
            continue

        print(elem)

    print()

    list_idx = 0
    while list_idx < len(list_v1):
        if not isinstance(list_v1[list_idx], int):
            list_idx += 1
            continue

        print(list_v1[list_idx])
        list_idx += 1


def break_statement():
    tuple_v1 = (547, "Python", True)
    list_v1 = [546, "I love python", tuple_v1]

    for elem in tuple_v1:
        if isinstance(elem, bool):
            break

        print(elem)
    else:
        print("For finish")

    print()

    list_idx = 0
    while list_idx < len(list_v1):
        if isinstance(list_v1[list_idx], tuple):
            break

        print(list_v1[list_idx])
        list_idx += 1


def nested_loops():
    tuple_v1 = (547, "Python", True)
    list_v1 = [546, "I love python", tuple_v1]

    for list_elem in list_v1:

        if isinstance(list_elem, tuple) or isinstance(list_elem, list):
            for nested_elem in list_elem:
                print(nested_elem)
        else:
            print(list_elem)


    """
    754, 743, 803, 783
    854, 243, 303, 983
    954, 943, 503, 873
    354, 343, 103, 738
    """

    matrix = [[754, 743, 803, 783],
              [854, 243, 303, 983],
              [954, 943, 503, 873],
              [354, 343, 103, 738]]

    print()
    for row in matrix:

        row_elems = ""
        for elem in row:

            if len(row_elems):
                row_elems += ", "

            row_elems += str(elem)

        print(row_elems)

nested_loops()
