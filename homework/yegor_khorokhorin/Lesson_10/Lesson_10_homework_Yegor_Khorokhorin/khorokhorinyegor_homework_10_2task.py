
def count_me(func):

    def wrapper(text, count):
        for x in range(count):
            func(text)
    return wrapper


@count_me
def example(text):
    print(text)


example('print me', count=5)
