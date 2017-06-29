from first_module import funcA


def test_funcA():
    assert funcA("foo") == "packagewdependency:module:funcA: foo"
