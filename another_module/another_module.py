from first_module import funcA
from simple_module import funcC


def funcB(x):
    return "packagewdependency:another_module:funcB: {}".format(x)


def allFuncs():
    print(funcA(funcB(funcC("successfully used this package and its dependency"))))
