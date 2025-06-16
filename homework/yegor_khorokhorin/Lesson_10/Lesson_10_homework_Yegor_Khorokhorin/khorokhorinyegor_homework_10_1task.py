def finish(func):

    def wrapper():
        func()
        print("finished")
    return wrapper


@finish
def example():
    print('example')


@finish
def example1():
    print('anything')


@finish
def example2():
    print(1+1)


example()
example1()
example2()

