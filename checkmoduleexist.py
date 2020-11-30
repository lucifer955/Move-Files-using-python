import importlib.util
import sys

#check if module is installed or not

moduleName = input("The module you want to check : ")

if moduleName in sys.modules:
    print(f"{moduleName!r} already in sys.modules")
else:
    answer = input(f"can't find the {moduleName!r} module, Do you want to import now (yes=1|no=0): ") 


if(answer == 1):
    if (spec := importlib.util.find_spec(moduleName)) is not None:
        # If you choose to perform the actual import ...
        module = importlib.util.module_from_spec(spec)
        sys.modules[moduleName] = module
        spec.loader.exec_module(module)
        print(f"{moduleName!r} has been imported")
    else:
        print(f"can't find the {moduleName!r} module")
else:
    print(f"{moduleName!r} has not been imported")
