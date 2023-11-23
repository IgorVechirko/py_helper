from .. import module_1
from pkg import module_2


def exported_func():
    module_1.exported_func()
    module_2.exported_func()
    print(__name__)