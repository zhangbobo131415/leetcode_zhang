try:
    raise EOFError
except EOFError:
    print("fds")
def time(func):
    def wraper():
        print('start')
        func()
        print('end')
    return wraper
@time
def f():
    print('ffff')
f()


