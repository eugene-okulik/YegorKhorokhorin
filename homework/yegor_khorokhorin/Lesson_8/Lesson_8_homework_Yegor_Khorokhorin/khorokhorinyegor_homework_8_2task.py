def progression():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


count = 1
for number in progression():
    if count == 5:
        print('Первое число:', number)
    elif count == 200:
        print('Второе число:', number)
    elif count == 1000:
        print('Третье число:', number)
    elif count == 100000:
        print('Четвертое число:', number)
        break
    count += 1
