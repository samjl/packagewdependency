from another_module import funcB


def test_funcB():
    assert funcB("foo") == "packagewdependency:another_module:funcB: foo"
