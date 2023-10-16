def foo():
    a = 10
    def bar():
        return a
    return bar()

#c = foo.func_core
print("wait")
print(foo.__code__.co_cellvars)
