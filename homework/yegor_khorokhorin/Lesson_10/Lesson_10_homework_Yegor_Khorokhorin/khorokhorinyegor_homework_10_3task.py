def operation_function(func):
    def wrapper(first, second):
        if first < 0 or second < 0:
            operation = '*'
        elif first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif second > first:
            operation = '/'
        else:
            raise ValueError('Error')
        return func(first, second, operation)
    return wrapper


@operation_function
def calc(first_number, second_number, operation):
    if operation == '+':
        return first_number + second_number
    elif operation == '-':
        return first_number - second_number
    elif operation == '*':
        return first_number * second_number
    elif operation == '/':
        return first_number / second_number


user_input_first = int(input("Введите первое число: "))
user_input_second = int(input("Введите второе число: "))

result = calc(user_input_first, user_input_second)
print(f"Результат: {result}")
