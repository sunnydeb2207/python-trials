def f1(x):
    def wrapper(a,b):
        print("test")
        if(b==0):
            print("0")
            return
    return wrapper

@f1
def f(a, b):
    print(a%b)
    return

t = f(3,0)))


