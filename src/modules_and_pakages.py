

def show_modules_search_paths():
    import sys

    num = 1
    for path in sys.path:
        print(f"{num}. {path}")
        num += 1


def import_affected_on_called_scope():
    num = 1
    for path in sys.path:
        print(f"{num}. {path}")
        num += 1


def module_attributes():
    import standalone_module

    print(standalone_module.__file__)


def import_module():
    import standalone_module
    import sys, os, threading

    print(standalone_module.exported_var)
    standalone_module.exported_func(1, "Hello standalone module")
    #print(exported_func)


def import_module_under_alias():
    import standalone_module as standalone
    print(standalone.exported_var)


def from_module_import():
    from standalone_module import exported_func, exported_var
    exported_func(43, 54)


def import_elem_undef_alias():
    from standalone_module import exported_var as exported
    print(exported)


"""from standalone_module import *
print(exported_var)
#print(_not_exported_var)
from standalone_module import _not_exported_var
print(_not_exported_var)"""


def using_importlib_to_reload_module():
    import standalone_module
    import standalone_module

    import importlib
    importlib.reload(standalone_module)


def import_module_from_package():
    import pkg.module_1
    from pkg import module_2
    from pkg import module_3 as third_module
    from pkg.module_4 import exported_func
    from pkg.nested.module_1 import exported_func as nested_exported_function

    pkg.module_1.exported_func()
    module_2.exported_func()
    third_module.exported_func()
    exported_func()
    nested_exported_function()


def import_pkg():
    import pkg
    #pkg.module_1.exported_func()
    import pkg_with_default_imports
    pkg_with_default_imports.module_1.exported_func()
    print(dir())


"""from pkg import *
#module_1.exported_func()
from pkg_with_default_imports import *
module_1.exported_func()"""


def import_conflict_solving():
    from pkg import module_1
    print(locals()["module_1"])
    from pkg_with_default_imports import module_1
    print(locals()["module_1"])

    module_1.exported_func()


def imports_in_package():
    import pkg.nested.module_1
    pkg.nested.module_1.exported_func()

imports_in_package()
"""

#import sys, module_scrip
#import module_scrip.exported_function  #Can't import with dot from standalone module

exported_var = 999
from standalone_module import exported_var
#from standalone_module import exported_var, exported_func

#from standalone_module import *
#print(_not_exported_var)

from standalone_module import exported_var_under_alias as alias
#print(alias)

import standalone_module as other_module
#print(other_module.exported_var)

import importlib
import standalone_module
importlib.reload(standalone_module)

#import pkg.module_1, pkg.module_2
#pkg.module_1.exported_func()
#pkg.module_2.exported_func()

#from pkg import module_1 as module_1_alias
#from pkg.module_1 import exported_func as module_1_extern_func











def import_in_function():
    from standalone_module import exported_func
    exported_func(1, 4)


def import_in_try_statement():
    try:
        import not_exixting_module
    except Exception:
        print("Can't import")"""
