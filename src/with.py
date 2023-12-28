
import sys
import threading
import contextlib

def with_using():
    with open(sys.argv[0]) as file:
        for line in file:
            print(line.rstrip())

    print("Is file closed", file.closed)


def with_using_2():
    lock = threading.Lock()
    with lock:
        print("Locked ", lock.locked())

    print("Locked ", lock.locked())


def context_lib_using():

    class Cursor:
        pass
    class DBConnection:
        def cursor(self):
            return Cursor()
        def commit(self):
            pass
        def rollback(self):
            pass


    @contextlib.contextmanager
    def db_transaction(connection):
        cursor = connection.cursor()
        try:
            yield cursor
        except:
            connection.rollback()
            raise
        else:
            connection.commit()

    connection = DBConnection()
    with db_transaction(connection) as cursor:
        pass


context_lib_using()
