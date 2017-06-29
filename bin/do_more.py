#!/usr/bin/env python
from first_module import funcA
from another_module import funcB
from simple_module import funcC


def main():
    print(funcA(funcB(funcC("Do more"))))

if __name__ == "__main__":
    main()
