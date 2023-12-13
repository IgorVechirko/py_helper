

def class_and_instances_attributes_and_func_access():

    print("Class suite executing")

    class Foo:
        public_class_attribute = ('Yellow', 4, False)
        __private_class_attribute = ('Yellow', 4, False)

        def class_func():
            print("class_func")

        def __private_class_func():
            print("__private_class_func")

        def __init__(self, arg1, arg2):
            self.instance_public_attribute = arg1
            self.__instance_private_attribute = arg2


        def execute(self):
            print(Foo.__private_class_attribute)
            Foo.__private_class_func()
            print(self.__instance_private_attribute)

    print(Foo.public_class_attribute)
    #print(Foo.__private_class_attribute)
    Foo.class_func()
    #Foo.__private_class_func()


    instance = Foo("arg1", "arg2")
    print(instance.instance_public_attribute)
    #print(instance.__instance_private_attribute)
    print(getattr(instance, "_Foo__instance_private_attribute"))

    instance.execute()


def super_usage():
    class Base:
        def execute(self):
            print("preparing...")

    class Child(Base):
        def execute(self):
            super(Child, self).execute()
            super().execute()
            print("doing something...")

    obj = Child()
    obj.execute()


def instantation():
    class Base:
        def __init__(self):
            print(self.__dict__)
            self.__base_attribute = "base attribute"
            print(self.__dict__)

    class Child(Base):
        def __init__(self):
            print(self.__dict__)
            super().__init__()
            self.__child_attribute = "child attribute"
            print(self.__dict__)

    obj = Child()


def method_resolution_order():
    class First:
        def __init__(self):
            self.__first = "first"

        def method(self ):
            print(self.__first)

    class Second(First):
        def __init__(self):
            super().__init__()
            self.__second = "second"

        def method(self):
            super().method()
            print(self.__second)

    class Third:
        def __init__(self):
            self.__third = "third"

        def method(self):
            print(self.__third)

    class Forth(Second, Third):
        def __init__(self):
            super(Forth, self).__init__()
            super(First, self).__init__()
            self.__forth = "forth"

        def method(self):
            super(First, self).method()
            print(self.__forth)
            super(Forth, self).method()



    print(Forth.__mro__)

    obj = Forth()
    obj.method()


def data_classes():
    import _dataclasses

    @dataclass
    class Point2:
        __x: int | float
        __y: int | float


def enum_classes():
    from enum import Enum

    class Color(Enum):
        YELLOW = 1
        RED = 2
        BLUE = 3

    print(Color.YELLOW)


def abstract_class():
    from abc import ABC, abstractmethod

    class AbstractBase(ABC):
        def __init__(self):
            self.__attribute = 1

        @abstractmethod
        def execute(self):
            pass


    class Concret(AbstractBase):
        def execute(self):
            print("implementation")

    obj = Concret()

