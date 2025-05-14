answer_1 = 'Результат операции: 42'
answer_2 = 'Результат операции: 54'
answer_3 = 'Результат работы программы: 209'
answer_4 = 'Результат: 2'

answers = [answer_1, answer_2, answer_3, answer_4]


def function(list_of_answers):
    for answer in list_of_answers:
        colon_index = answer.index(":")
        number_str = answer[colon_index + 1:].strip()
        result = int(number_str) + 10
        print(f"Результат после прибавления 10: {result}")


function(answers)
