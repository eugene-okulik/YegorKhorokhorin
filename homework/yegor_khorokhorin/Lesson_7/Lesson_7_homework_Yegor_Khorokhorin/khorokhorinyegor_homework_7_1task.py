# import random
# x = random.randint(1, 10) # Можно так с рандомным числом отдаваемым программой
x = 5
while True:
    user_input = input('Enter number: ')
    if int(user_input) == x:
        print("Поздравляю! Вы угадали!")
        break
    elif int(user_input) != x:
        print('Попробуйте снова')
print('Good bye!')
