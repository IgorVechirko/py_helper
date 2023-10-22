
class CustomException(Exception):
    def __init__(self, *argv):
        super().__init__(*argv)


def raise_exception(divided_and_divisor):
    print("Division start")
    x = divided_and_divisor[0] / divided_and_divisor[1]
    print("Division finish")

    raise CustomException("This", "is", "custom", "exception")


def typed_and_instanced_exception(typed):
    if typed:
        raise Exception
    else:
        raise CustomException()


def catch_concrete_exception():
    try:
        raise_exception((5,))
    except ZeroDivisionError:
        print("Oops, that was invalid math operation")


def catch_multiple_exceptions():
    try:
        raise_exception((5, 0))
    except ZeroDivisionError:
        print("Oops, that was invalid math operation")
    except IndexError:
        print("Oops, seems like you go out of range")


def catch_multiple_exceptions_in_one_statement():
    try:
        raise_exception((5,))
    except (ZeroDivisionError, IndexError):
        print("Oops, can't do division")


def catch_all_exceptions():
    try:
        raise_exception((5, "5.5"))
    except (ZeroDivisionError, IndexError):
        print("Oops, can't do division")
    except Exception:
        print("Oops, some other problem")


def catch_exception_object():
    try:
        raise_exception((5, 5))
    except Exception as exp:
        print(type(exp))
        print(exp.args)
        print(exp)


def catch_inherited_exceptions():
    try:
        raise_exception((5, 5))
    except Exception:
        print("Catch Exception")
    except CustomException:
        print("Catch custom exception")


def dont_catch_critical_exceptions():
    try:
        exit(-1)
    except Exception:
        print("Not critical exception occur")
    #except BaseException:
    #    print("You should not catch these exceptions")


def reraise_exception():
    try:
        raise_exception((5,0))
    except Exception as exp:
        print("Catch exception {} first time".format(exp))
        raise

def catch_reraised_exception():
    try:
        reraise_exception()
    except Exception as exp:
        print("Catch exception {} second time".format(exp))


def else_clause():
    try:
        division = 5 / 0
    except Exception:
        print("Exception")
        raise
    else:
        print("No exceptions")


def finally_clause():
    try:
        print("Here we work with resources which we must free after complete 'try' no meter is exception will raise or not")
        raise CustomException()
    except Exception:
        print("Exception was occur")
    finally:
        print("Free captured resources")


def exception_chaining():
    try:
        raise_exception((5, 5))
    except CustomException:
        raise Exception("Raise another exception inside except block")


def restrict_exception_chaining():
    try:
        raise_exception((5, 5))
    except CustomException:
        raise Exception("Raise another exception inside except block") from None



