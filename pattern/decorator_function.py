def f1(f):
    def wrapper(*args,**kwargs):
        print("before f")
        ret = f(*args,**kwargs)
        print("after f")
        return ret
    return wrapper

@f1
def f(a):
    print(a)
    return a

print(f("Hi!"))